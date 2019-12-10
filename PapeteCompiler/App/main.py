import sys
import antlr4

from App.Grammar.PapeteLexer import PapeteLexer
from App.Grammar.PapeteParser import PapeteParser
from App.Grammar.PapeteVisitor import PapeteVisitor


variables = {

}


class CustomVisitor(PapeteVisitor):
    pass
    # """
    #     Fatores:
    # """

    # def visitNumIntFact(self, ctx: PapeteParser.NumIntFactContext):
    #     node = ctx.NUMINT()
    #     print("NumInt",node.getText())
    #     return int(node.getText())

    # def visitNumDoubleFact(self, ctx: PapeteParser.NumDoubleFactContext):
    #     node: antlr4.TerminalNode = ctx.NUMDOUBLE() 
    #     return float(node.getText())

    # def visitVarFact(self, ctx: PapeteParser.VarFactContext):
    #     # Todo: check if logic is correct later on;
    #     text = ctx.VAR().getText()
    #     if text in variables:
    #         return variables[text]
    #     else:
    #         raise Exception()

    # """
    #     Termos:
    # """

    # def visitMultTerm(self, ctx: PapeteParser.MultTermContext):
    #     return self.visit(ctx.term()) * self.visit(ctx.expr())

    # def visitDivTerm(self, ctx: PapeteParser.DivTermContext):
    #     return self.visit(ctx.term()) / self.visit(ctx.fact())

    # def visitRestTerm(self, ctx: PapeteParser.RestTermContext):
    #     return self.visit(ctx.term()) % self.visit(ctx.fact())

    # # def visitFactTerm() - base implemented;

    # """
    #     Expressões:
    # """

    # def visitSumExpr(self, ctx: PapeteParser.SumExprContext):
    #     return self.visit(ctx.expr()) + self.visit(ctx.term())

    # def visitMinusExpr(self, ctx: PapeteParser.MinusExprContext):
    #     return self.visit(ctx.expr()) - self.visit(ctx.term())

    # # def visitTermExpr() - base implemented;

    # def visitIntAtr(self, ctx: PapeteParser.IntAtrContext):

    #     print("int:", ctx.VAR())
    #     #raise NotImplementedError()
    #     return self.visitChildren(ctx)

    # def visitDoubleAtr(self, ctx: PapeteParser.DoubleAtrContext):
    #     print("double:", ctx.VAR())
    #     return self.visitChildren(ctx)

    # def visitAtrLine(self, ctx: PapeteParser.AtrLineContext):
    #     # #help(ctx.atr())
    #     # print(dir(ctx.atr()))
    #     # #self.visitIntAtr(ctx.atr())
    #     # #self.visitDoubleAtr(ctx.atr())
    #     return self.visitChildren(ctx)


def main():
    if(len(sys.argv) <= 1):
        print("Missing input argument...")
        return
    filename = sys.argv[1]
    input_stream = antlr4.FileStream(filename)
    lexer = PapeteLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = PapeteParser(stream)
    tree = parser.prog()

    print("Visiting...")
    print(tree.toStringTree())
    #print(tree.getRuleIndex())
    visitor = CustomVisitor()
    visitor.visit(tree)
    #walker = antlr4.ParseTreeWalker()
    #walker.walk(listener, tree)

    # print(tree.toStringTree())


if __name__ == "__main__":
    main()
