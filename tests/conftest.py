import os
import tempfile

import pytest

from jupynium import pynvim_helpers
from jupynium.buffer import JupyniumBuffer


@pytest.fixture(scope="session")
def jupbuf1():
    return JupyniumBuffer(["a", "b", "c", "'''%%%", "d", "%%'''", "f"])


@pytest.fixture(scope="session")
def nvim_1():
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "nvim")
        os.system(f"nvim --clean --headless --listen {path} &")
        nvim = pynvim_helpers.attach_and_init(path)

        yield nvim

        # Teardown
        nvim.quit()
