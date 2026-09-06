#!/usr/bin/env python3
"""One supervised A1/A3 rerun, using the unchanged first-run capture harness."""
import importlib.util
from pathlib import Path
import sys

sys.dont_write_bytecode = True
out = Path(__file__).resolve().parent
source = out.parent / '2026-09-06-response-modes/run-cases.py'
spec = importlib.util.spec_from_file_location('fp_native_capture', source)
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)
runner.OUT = out
runner.ORDER = ['A1', 'A3']
runner.main()
