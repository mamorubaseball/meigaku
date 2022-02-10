'''
コンテキストプロセッサーとは
変数をビューからテンプレートに直接渡さなくても、
テンプレート上で変数を扱えるよういする仕組み　　
'''
from .models import Category
def common(request):
    category_data=Category.objects.all()
    context={
        'category_data':category_data,
    }
    return context
