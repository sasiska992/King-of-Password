from .all_in_one import AllIn
from loader import dp
from .throttling import TrottlingMiddleWare
from .acl import ACLMiddleware
from .post_acl import PostACL

if __name__ == "middle_wares":
    dp.middleware.setup(ACLMiddleware())
    dp.middleware.setup(PostACL())
    dp.middleware.setup(AllIn())
    dp.middleware.setup(TrottlingMiddleWare())
