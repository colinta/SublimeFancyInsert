FancyInsert plugin
==================

A basic "insert template string".  Supports:

- `file_name`: Easy
- `path`: The full path
- `classname`: camel-cased version of the file_name
- `project`: If you're not using a project, it defaults to the folder name
- `day`: (numeric) day of month
- `month`: "
- `year`: "



Installation
------------

1. Using Package Control, install "FancyInsert"

Or:

1. Open the Sublime Text Packages folder
    - OS X: ~/Library/Application Support/Sublime Text 3/Packages/
    - Windows: %APPDATA%/Sublime Text 3/Packages/
    - Linux: ~/.Sublime Text 3/Packages/ or ~/.config/sublime-text-3/Packages

2. clone this repo
3. Install keymaps for the commands (see Example.sublime-keymap for my preferred keys)

Commands
--------

To use this plugin, create files in `[package path]/User/FancyInsert`, e.g. `/Users/your_username/Library/Application Support/Sublime Text 3/Packages/User/FancyInsert`.  The name of the file is important; it will become the "tab trigger".  The extension will be used to match the syntax.  Some extensions (like `js`) that don't match the syntax name (`source.javascript`) are supported, but not all.  If it seems like your snippet doesn't work, use the "Show Scope Name", and look for `source.foo` <- `foo` would be the extension.  No extension is a "global" snippet.

The file can contain python's `string.format`-style macros, but they can *also* contain Sublime's snippet syntax.  This means that in order to insert `${1:foo}`, you have to "escape" the curly brackets, e.g. `${{1:foo}}`.

Here's an example, I use it for "class.swift", so in a swift file, `class[tab]` will activate this snippet:

```
/***
 *  {file_name}
***/

${{1:class}} ${{2:{classname}}} {{$0
}}
```

When activated in "MyClass.swift", this snippet produces:

```swift
/***
 *  MyClass.swift
***/

class MyClass {
}
```
