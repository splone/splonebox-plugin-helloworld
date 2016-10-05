"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
#!/usr/bin/env python

from splonebox.api.plugin import RemoteFunction
from splonebox.api.plugin import Plugin

__author__ = "mkind"
NAME="hello world"
DESC="my description"
LICENSE="GPLv3"
DEBUG=True

@RemoteFunction
def helloworld():
    return """
And these children that you spit on
As they try to change their worlds
Are immune to your consultations
They're quite aware of what they're goin' through

David Bowie
"""

if __name__ == "__main__":
    p = Plugin(NAME, DESC, __author__, LICENSE, DEBUG)
    p.connect("127.0.0.1", 6666)
    p.register()

