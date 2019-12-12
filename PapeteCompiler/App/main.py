import sys
import antlr4

from App.Grammar.PapeteLexer import PapeteLexer
from App.Grammar.PapeteParser import PapeteParser
from App.Grammar.PapeteVisitor import PapeteVisitor
from App.Grammar.PapeteListener import PapeteListener
from App.PapeteVisitorImpl import PapeteVisitorImpl
from App.PapeteVisitorImpl import log
from App.PapetePreprocessor import import_files_now
parser = None


class CustomListener(PapeteListener):
    def enterEveryRule(self, ctx):
        global parser
        log(
            f"text={ctx.getText()} || rule={parser.ruleNames[ctx.getRuleIndex()]}")


def main():
    if(len(sys.argv) <= 1):
        log("Missing input argument...")
        return
    global parser

    filename = sys.argv[1]
    # Preprocesses;
    datastream = import_files_now(filename)

    input_stream = antlr4.InputStream(datastream)
    lexer = PapeteLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = PapeteParser(stream)
    tree = parser.prog()

    log("Visiting...")
    # log(tree.toStringTree())

    def visit():
        visitor = PapeteVisitorImpl()
        visitor.visit(tree)
        log(visitor.mhandler)

    def walk():
        listener = CustomListener()
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)

    # walk()
    visit()


if __name__ == "__main__":
    main()
