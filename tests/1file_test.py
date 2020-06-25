# -*- coding: utf-8 -*-
"""Tests for file operations"""
# standard library imports
import shutil
from pathlib import Path

# first-party imports
import pytest
import sh

# module imports
# local imports
from . import working_directory

# global constants
alphabetsoup = sh.Command("alphabetsoup")

# global constants
TEST_FILES = ["P450s.faa", "ribosylation.faa", "short.faa"]


def test_setup(request):
    """Remove datadir, if it exists, and install copies of static data."""
    testdir = Path(request.fspath.dirpath())
    datadir = testdir / "data"
    if datadir.exists():
        shutil.rmtree(datadir)  # remove anything left in data directory
    filesdir = testdir / "testdata"
    shutil.copytree(filesdir, datadir)


def test_data_commands(datadir_mgr):
    """Test sequence of commands."""
    tests = [
        [
            "--dedup",
            "--no-log",
            "--first_n",
            "1",
            "--log",
            "--lengths",
            "-v",
            ".",
        ],
        ["--minlen", "200", "--no-stripdash", "-q", "."],
        ["-v", "."],
        ["--defrag", "--overwrite", "--progress", "--maxambig", "1", "."],
    ]
    with datadir_mgr.in_tmp_dir(inpathlist=TEST_FILES):
        for test_args in tests:
            print(test_args)
            try:
                output = alphabetsoup(test_args)
            except sh.ErrorReturnCode as errors:
                print(errors)
                pytest.fail(f"Test failed with args {test_args}")
            print(output)
            assert Path("log/alphabetsoup.log").exists()
        assert Path("log/alphabetsoup_stats.tsv").exists()
