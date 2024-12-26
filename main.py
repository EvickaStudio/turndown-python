from src.turndown import TurndownService

td = TurndownService({"headingStyle": "atx", "codeBlockStyle": "fenced"})

html = "<h1>Hello, World!</h1>"
markdown = td.turndown(html)
print(markdown)
# # Hello, World!

html = """<p>Here's a blockquote:</p>
<blockquote>Contents should not be swallowed. This is due to the enormous amount of harmful chemicals that has gone into this burger.</blockquote>
<p>That was a blockquote.</p>"""

markdown = td.turndown(html)
print(markdown)
# Here's a blockquote:

# > Contents should not be swallowed. This is due to the enormous amount of harmful chemicals that has gone into this burger.

# That was a blockquote.
