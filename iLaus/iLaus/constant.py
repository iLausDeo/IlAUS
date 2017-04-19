# coding: utf-8


class UGConst(object):
    '''
    自定义常量
    '''
    _instance = None
    def __new__(cls, *args, **kw):
        if not cls._instance:
            cls._instance = super(UGConst, cls).__new__(cls, *args, **kw)
        return cls._instance
    class ConstError(TypeError):
        pass
    class ConstCaseError(ConstError):
        pass
    def __setattr__(self, name, val):
        if name in self.__dict__:
            raise self.ConstError("Can't change const.{}".format(name))
        if not name.isupper():
            raise self.ConstCaseError("const name {} is not all uppercase".format(name))
        self.__dict__[name] = val


const = UGConst()
const.SUCCESS_STATUS = 9200
const.NOTFOUND_STATUS = 9400
const.NOTFOUND_FIELD_STATUS = 9401