#-*- coding: utf-8 -*-
'''
�������չʾ�����Դ����Ƕ��doctest������
'>>>' ��ͷ���о���doctest����������
���� '>>>' ���о��ǲ��������������
���ʵ�����еĽ���������Ľ����һ�£��ͱ��Ϊ����ʧ�ܡ�
'''
def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)