from __future__ import print_function

from django.http import JsonResponse, HttpResponse

from app_dir.main.forms import *
from app_dir.main.conditional_forms import *
import ast
import copy
import os


def convertExpr2Expression(Expr):
    Expr.lineno = 0
    Expr.col_offset = 0
    result = ast.Expression(Expr.value, lineno=0, col_offset=0)

    return result


def exec_with_return(code):
    code_ast = ast.parse(code)

    init_ast = copy.deepcopy(code_ast)
    init_ast.body = code_ast.body[:-1]

    last_ast = copy.deepcopy(code_ast)
    last_ast.body = code_ast.body[-1:]

    exec(compile(init_ast, "<ast>", "exec"), globals())
    if type(last_ast.body[0]) == ast.Expr:
        return eval(compile(convertExpr2Expression(last_ast.body[0]), "<ast>", "eval"), globals())
    else:
        exec(compile(last_ast, "<ast>", "exec"), globals())


def create_app(request):
    if request.is_ajax():
        code = request.POST['code']
        result = exec_with_return(code)
    else:
        return HttpResponse('Use ajax format!')

    return JsonResponse({'code': result})


def custom_app(param0, param1, param2):
    param0 = param0
    os.remove("templates/app.html")
    f = open("templates/app.html", "a+")
    f.write(param0)
    f.close()

    param1 = param1
    f = open("templates/app.html", "a+")
    f.write(param1)
    f.close()
    f.close()
    param2 = param2
    f = open("templates/app.html", "a+")
    f.write(param2)
    f.close()
    f.close()
