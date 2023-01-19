import os.path
import sublime
import sublime_plugin
import datetime


class FancySnippetListener(sublime_plugin.EventListener):
    def on_text_command(self, view, command_name, args):
        if command_name == 'auto_complete' and len(view.sel()) == 1:
            sel = view.sel()[0]
            commands = {
                'copy': ('fancy_insert_copyright', {'name': 'copy'}),
                'spec': ('fancy_insert_spec', {'name': 'spec'}),
                'appl': ('fancy_insert_apple', {'name': 'appl'}),
                'aapl': ('fancy_insert_apple', {'name': 'aapl'}),
            }

            for (name, command) in commands.items():
                command_len = len(name)
                args = {}
                if sel.a == command_len and sel.b == command_len and view.substr(sublime.Region(0, command_len)) == name:
                    return command


class FancyInsertCommand(sublime_plugin.TextCommand):
    def default_keys(self):
        view = self.view
        path = view.file_name()
        project_path = view.window().project_file_name() or 'Untitled'
        project = os.path.basename(project_path).replace('.sublime-project', '')

        project_path = view.window().project_file_name()
        project = None
        if project_path:
            project = os.path.basename(project_path).replace('.sublime-project', '')

        if not project:
            if path:
                project = os.path.basename(os.path.dirname(path))
            else:
                project = 'Untitled'

        filename = view.file_name()
        if filename:
            filename = os.path.basename(filename)
            classname = os.path.splitext(filename)[0]
        else:
            filename = 'Untitled'
            classname = filename
        today = datetime.date.today()
        day, month, year = (today.day, today.month, today.year)

        return {
            'file_name': filename,
            'classname': classname,
            'project': project,
            'day': day,
            'month': month,
            'year': year
        }


class FancyInsertCopyrightCommand(FancyInsertCommand):

    def run(self, edit, name):
        template = '''
////
///  {file_name}
//

${{1:class}} ${{2:{classname}}} {{$0
}}
'''[1:]
        contents = template.format(**self.default_keys())
        self.view.replace(edit, sublime.Region(0, len(name)), '')
        self.view.run_command('insert_snippet', {'contents': contents})


class FancyInsertSpecCommand(FancyInsertCommand):

    def run(self, edit, name):
        keys = self.default_keys()
        file_name = keys['file_name']
        classname_spec = os.path.splitext(file_name)[0]
        classname = classname_spec.replace('Spec', '')
        keys['classname_spec'] = classname_spec
        keys['classname'] = classname
        template = '''
////
///  {file_name}
//

@testable import {project}
import Quick
import Nimble


class {classname_spec}: QuickSpec {{
    override func spec() {{
        describe("${{1:{classname}}}") {{
            it("$0") {{
            }}
        }}
    }}
}}
'''[1:]
        contents = template.format(**keys)
        self.view.replace(edit, sublime.Region(0, len(name)), '')
        self.view.run_command('insert_snippet', {'contents': contents})


class FancyInsertAppleCommand(FancyInsertCommand):

    def run(self, edit, name):
        template = '''
//
//  {file_name}
//  {project}
//
//  Created by Colin Gray on {month}/{day}/{year}.
//  Copyright © {year} Nicolette. All rights reserved.
//

${{1:class}} ${{2:{classname}}} {{$0
}}
'''[1:]
        contents = template.format(**self.default_keys())
        self.view.replace(edit, sublime.Region(0, len(name)), '')
        self.view.run_command('insert_snippet', {'contents': contents})
