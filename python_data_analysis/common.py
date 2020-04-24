def eval_and_print(expr, eval_globals=None, eval_locals=None):
    print("{}:\n{}".format(expr, eval(expr, eval_globals, eval_locals)))