# Tool gaps encountered

- `node_modules/@rig-c/parts/docs/MOTION.md` is referenced by the package's documentation index but is absent from the installed package. The attempted `cat` returned `No such file or directory`; motion work continued using the installed authoring docs and rigging docs.
- `node_modules/.bin/rig-parts assemble --help` is not supported. It returned a usage error listing the accepted assemble flags and directing users to `rig-parts --help`; command discovery continued with global help.
- `@esotericsoftware/spine-core` is declared as a development dependency of `@rig-c/parts` but is not installed in this exam's node_modules. The grader log reports that spine-core round-trip commands are unavailable. Core `spine-html` checks did run, but this missing package limited the comparison build path.
