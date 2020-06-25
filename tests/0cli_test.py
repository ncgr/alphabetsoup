# -*- coding: utf-8 -*-
"""Tests for basic CLI function."""
# first-party imports
import pytest
import sh

# module imports
# local imports
from . import working_directory

# global constants
alphabetsoup = sh.Command("alphabetsoup")


def test_cli(tmp_path):
    """Test basic cli function."""
    with working_directory(tmp_path):
        try:
            output = alphabetsoup(["--help"])
        except sh.ErrorReturnCode as errors:
            print(errors)
            pytest.fail("Basic cli test failed")
        print(output)
        assert "Usage:" in output
        assert "Options:" in output


def test_version(tmp_path):
    """Test version command."""
    with working_directory(tmp_path):
        try:
            output = alphabetsoup(["--version"])
        except sh.ErrorReturnCode as errors:
            print(errors)
            pytest.fail(errors)
        print(output)
        assert "version" in output
