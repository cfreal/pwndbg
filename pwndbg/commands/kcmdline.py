import argparse

import pwndbg.commands
import pwndbg.gdblib.kernel

parser = argparse.ArgumentParser(description="Return the kernel commandline (/proc/cmdline)")


@pwndbg.commands.ArgparsedCommand(parser)
@pwndbg.commands.OnlyWhenQemuKernel
@pwndbg.commands.OnlyWithKernelDebugSyms
def kcmdline():
    print(pwndbg.gdblib.kernel.kcmdline())