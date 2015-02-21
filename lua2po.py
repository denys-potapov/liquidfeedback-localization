#!/usr/bin/env python
import fileinput
import re




messages = {}

for line in fileinput.input():
	match = re.match( r'\[(.*)\]\s=\s(.*);', line)
	if not match:
		continue
	msgid = match.group(1)
	msgstr = match.group(2)
	if msgstr == 'false':
		msgstr = '""'
	messages[msgid] = msgstr
	
print 'msgid ""'
print 'msgstr ""'
print '"Content-Type: text/plain; charset=UTF-8\\n"'
print '"Content-Transfer-Encoding: 8bit\\n"'

for msgid in messages:
	print ''
	print 'msgid ' + msgid
	print 'msgstr ' + messages[msgid]
