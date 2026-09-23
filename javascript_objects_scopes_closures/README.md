# alu-higher_level_programming

## JavaScript - Objects, Scopes and Closures

### Description

This directory covers more advanced JavaScript concepts: defining classes with the `class` keyword, working with objects and their prototypes, understanding variable scope (`let`, `const`, and block scope), and closures. Each script is written to comply with the `semistandard` linter.

### Requirements

- All scripts are interpreted/compiled on Ubuntu 20.04 LTS using Node.js (version 14.x or later)
- All files end with a new line
- A `README.md` file, at the root of the project folder, is mandatory
- The first line of all files should begin with `#!/usr/bin/node`
- All code should use the `const` and `let` keywords — `var` is not allowed
- All code should use the `class` keyword when defining a class (no old-style prototype-based classes)
- All code should pass `semistandard` (with no warnings)
- To test `semistandard`, run: `semistandard file_name.js`

### Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `0-rectangle.js` | An empty `Rectangle` class, defined using the `class` keyword |

### Usage

Files that export a class or function are meant to be used with `require`, for example:

```javascript
const Rectangle = require('./0-rectangle');
const r1 = new Rectangle();
console.log(r1);
```

### Author

This project is part of the ALX Software Engineering program, Higher-Level Programming track.
