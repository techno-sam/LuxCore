#!/usr/bin/python3.11

"""Tool for easier link debugging"""

import os

DIR = "/home/sam/LuxCoreWork/LinuxCompile/LuxCore/samples/luxcoredemo/"
F_LINK = "CMakeFiles/luxcoredemo.dir/link.txt"
F_LINK_NL = "CMakeFiles/luxcoredemo.dir/link_newline.txt"
F_LINK_GEN = "CMakeFiles/luxcoredemo.dir/link_generated.txt"

os.chdir(DIR)

if not os.path.exists(F_LINK_NL):
    print("Generating newline file")

    with open(F_LINK, encoding="utf8") as f:
        pieces1 = f.read().split(" ")

    with open(F_LINK_NL, "w", encoding="utf8") as f:
        f.write("\n".join(pieces1))
else:
    print("Recombining newline file")

    with open(F_LINK_NL, encoding="utf8") as f:
        pieces = f.read().split("\n")
    pieces = [piece for piece in pieces if not piece.startswith("#")]

    with open(F_LINK_GEN, "w", encoding="utf8") as f:
        f.write(" ".join(pieces))

    print("Running linker")
    os.system(f"cd {DIR} && "
              f"/usr/bin/cmake -E cmake_link_script {F_LINK_GEN} "
              f"--verbose=1")
