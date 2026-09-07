import contextlib
import io
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch
import live_loop
FLAGS='--bare --tools --disallowedTools --max-budget-usd --max-turns --output-format --strict-mcp-config'
class LiveController(unittest.TestCase):
    def run_case(self,responses):
        with tempfile.TemporaryDirectory() as d:
            root=Path(d);(root/'data').mkdir();(root/'data/meeting.txt').write_text('fictional fixture')
            completed=[subprocess.CompletedProcess([],0,FLAGS,'')]+responses
            with patch.dict(live_loop.os.environ,{'ANTHROPIC_API_KEY':'test-placeholder-not-a-key'}),patch.object(live_loop,'ROOT',root),patch.object(live_loop.shutil,'which',return_value='/fake/claude'),patch.object(live_loop.subprocess,'run',side_effect=completed) as run,contextlib.redirect_stdout(io.StringIO()):
                code=live_loop.main()
            trace=json.loads((root/'output/live/trace.json').read_text())
            calls=run.call_args_list[1:]
            for call in calls:
                args=call.args[0]
                self.assertEqual(args[args.index('--tools')+1],'')
                self.assertEqual(args[args.index('--max-turns')+1],'1')
                self.assertEqual(call.kwargs['timeout'],120)
            return code,trace,len(calls)
    def result(self,file):
        return subprocess.CompletedProcess([],0,json.dumps({'result':(live_loop.ROOT/'examples'/file).read_text()}),'')
    def test_failure_then_success_stops(self):
        c,t,n=self.run_case([self.result('summary.bad.json'),self.result('summary.good.json')]);self.assertEqual((c,t['status'],n),(0,'DONE',2))
    def test_exhaustion_is_escalation(self):
        c,t,n=self.run_case([self.result('summary.bad.json')]*3);self.assertEqual((c,t['status'],n),(2,'ESCALATED',3))
    def test_cli_failure_does_not_retry(self):
        c,t,n=self.run_case([subprocess.CompletedProcess([],1,'','failure')]);self.assertEqual((c,t['status'],n),(2,'ESCALATED',1))
    def test_timeout_escalates(self):
        c,t,n=self.run_case([subprocess.TimeoutExpired('claude',120)]);self.assertEqual((c,t['status'],n),(2,'ESCALATED',1))
