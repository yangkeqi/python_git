import logging
import time

def Log_Maker(level, msg):
    #创建Logger对象
    logger_obj = logging.getLogger("Test")
    #logger_obj=logging.Logger("crm_logger")
    logger_obj.setLevel(logging.DEBUG)

    #创建FileHandler对象  localhost.2019-11-08.log
    filehandler_obj = logging.FileHandler("ErrorLog%s" % time.strftime("%Y-%m-%d %H：%M：%S", time.localtime()))

    #创建Formatter对象
    formatter_obj = logging.Formatter(fmt="%(asctime)s %(filename)s %(funcName)s %(levelname)s %(lineno)d %(module)s  %(name)s  %(pathname)s %(message)s")

    #将Formatter对象加载到filehandler对象中
    filehandler_obj.setFormatter(formatter_obj)

    #将filehandler对象加载到Logger对象中
    logger_obj.addHandler(filehandler_obj)

    #输出日志
    if level.upper() == "DEBUG":
        logger_obj.debug(msg)

    elif level.upper() == "INFO":
        logger_obj.info(msg)

    elif level.upper() == "WARNING":
        logger_obj.warning(msg)

    elif level.upper() == "ERROR":
        logger_obj.error(msg)

    elif level.upper() == "CRITICAL":
        logger_obj.critical(msg)
    else:
        raise TypeError('输入类型错误！')

    logger_obj.removeHandler(filehandler_obj)
