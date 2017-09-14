# coding: utf-8
"""
General skin settings
"""
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from askbot.conf.settings_wrapper import settings
from askbot.deps.livesettings import ConfigurationGroup
from askbot.deps.livesettings import values
from django.utils.translation import ugettext_lazy as _
from askbot.skins import utils as skin_utils
from askbot import const
from askbot.conf.super_groups import CONTENT_AND_UI

WORDS = ConfigurationGroup(
                    'WORDS',
                    _('Site terms vocabulary'),
                    super_group = CONTENT_AND_UI
                )

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_YOUR_QUESTION',
        # lxw
        # default=_('Ask Your Question'),
        default=_('提问'),
        # description=_('Ask Your Question'),
        description=_('提问'),
        help_text=_('Used on a button'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_THE_GROUP',
        # lxw
        # default=_('Ask the Group'),
        default=_('小组提问'),
        # description=_('Ask the Group'),
        description=_('小组提问'),
        help_text=_('Used on a button'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_POST_YOUR_ANSWER',
        # lxw
        # default=_('Post Your Answer'),
        # description=_('Post Your Answer'),
        default=_('提交回答'),
        description=_('提交回答'),
        help_text=_('Used on a button'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_YOUR_OWN_QUESTION',
        # lxw
        # default=_('Answer Your Own Question'),
        # description=_('Answer Your Own Question'),
        default=_('回答自己的问题'),
        description=_('回答自己的问题'),
        help_text=_('Used on a button'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_ANSWER_OWN_QUESTION',
        #default=_(
            '<span class="big strong">You are welcome to answer your own question</span>, '
            'but please make sure to give an <strong>answer</strong>. '
            'Remember that you can always <strong>revise your original question</strong>.'
        ),
        default=_(
            '<span class="big strong">你可以对自己的问题进行回答</span>, '
            '但请确保给出一个<strong>答案</strong>. '
            '你可以随时<strong>修改你之前提问的问题</strong>.'
        ),
        #description=_('Instruction to answer own questions'),
        description=_('我们个人问题的介绍'),
        help_text=_('HTML is allowed'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_POST_ANONYMOUSLY',
        #default=_(
            '<span class="strong big">Please start posting anonymously</span> - '
            'your entry will be published after you log in or create a new account.'
        ),
        default=_(
            '<span class="strong big">开始匿名发帖</span> - '
            '在你登入或创建帐户之后，你的登录会被发布.'
        ),
        #description=_('Instruction to post anonymously'),
        description=_('匿名发帖介绍'),
        help_text=_('HTML is allowed'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_TO_GIVE_ANSWERS',
        #default=_(
            'This space is reserved only for answers. '
            'If you would like to engage in a discussion, '
            'please instead post a comment under the question or '
            'an answer that you would like to discuss'
        ),
        default=_(
            '该地仅用于回答问题. '
            '如果你想参与讨论, '
            '在问题下面发表你的评论 或者 '
            '在你想讨论的回答下面发表评论'
        ),
        #description=_('Instruction to give answers'),
        description=_('回答问题介绍'),
        help_text=_('HTML is allowed'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_INSTRUCTION_FOR_THE_CATEGORY_SELECTOR',
        #default=_(
            'Categorize your question using this tag selector or '
            'entering text in tag box.'
        ),
        default=_(
            '用标签选取器将你的问题归类或者 '
            '在标签栏输入文本.'
        ),
        #description=_('Instruction for the category selector'),
        description=_('归类选取器介绍'),
        help_text=_('Plain text only'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_YOUR_PREVIOUS_ANSWER',
        # lxw
        # default=_('Edit Your Previous Answer'),
        # description=_('Edit Your Previous Answer'),
        default=_('编辑之前的回答'),
        description=_('编辑之前的回答'),
        help_text=_('Used on a button'),
        localized=True
    )
)

#action definition (action def)
#this phrase is used as a parameter within 
#another phrase like "sorry, you cannot ask questions"
#hopefully it works, because it is used in indefinite form
#other similarly used phrases are marked as "action def" below
settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_QUESTIONS',
        # lxw
        # default=_('ask questions'),
        # description=_('ask questions'),
        default=_('提问'),
        description=_('提问'),
        localized=True
    )
)

#action def
settings.register(
    values.StringValue(
        WORDS,
        'WORDS_POST_ANSWERS',
        # lxw
        # default=_('post answers'),
        # description=_('post answers'),
        default=_('回答'),
        description=_('回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_MERGE_QUESTIONS',
        # lxw
        # default=_('Merge duplicate questions'),
        # description=_('Merge duplicate questions'),
        default=_('合并重复的问题'),
        description=_('合并重复的问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ENTER_DUPLICATE_QUESTION_ID',
        # lxw
        # default=_('Enter duplicate question ID'),
        # description=_('Enter duplicate question ID'),
        default=_('输入重复问题的ID'),
        description=_('输入重复问题的ID'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED',
        # lxw
        # default=_('asked'),
        # description=_('asked'),
        default=_('提问时间'),
        description=_('提问时间'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_FIRST_QUESTION',
        # lxw
        # default=_('Asked first question'),
        # description=_('Asked first question'),
        default=_('提问第一个问题'),
        description=_('提问第一个问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_BY_ME',
        # lxw
        # default=_('Asked by me'),
        # description=_('Asked by me'),
        default=_('我的提问'),
        description=_('我的提问'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASKED_A_QUESTION',
        # lxw
        # default=_('Asked a question'),
        # description=_('Asked a question'),
        default=_('提问问题'),
        description=_('提问问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_A_QUESTION',
        # lxw
        # default=_('Answered a question'),
        # description=_('Answered a question'),
        default=_('回答问题'),
        description=_('回答问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_BY_ME',
        # lxw
        # default=_('Answered by me'),
        # description=_('Answered by me'),
        default=_('我的回答'),
        description=_('我的回答'),
        localized=True
    )
)


settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPTED_AN_ANSWER',
        # Lxw 
        #default=_('accepted an answer'),
        #description=_('accepted an answer'),
        default=_('接受一个回答'),
        description=_('接受一个回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GAVE_ACCEPTED_ANSWER',
        # Lwx
        #default=_('Gave accepted answer'),
        #description=_('Gave accepted answer'),
        default=_('给被接受的答案'),
        description=_('给被接受的答案'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED',
        # lxw
        # default=_('answered'),
        # description=_('answered'),
        default=_('回答时间'),
        description=_('回答时间'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_QUESTIONS_COUNTABLE_FORMS',
        #default=_('question\nquestions'),
        #description=_('Countable plural forms for "question"'),
        default=_('问题\n问题'),
        description=_('“问题”的可数名词复数'),
        help_text=_('Enter one form per line, pay attention'),
        localized=True
    )
)

settings.register(
    values.LongStringValue(
        WORDS,
        'WORDS_ANSWERS_COUNTABLE_FORMS',
        #default=_('answer\nanswers'),
        #description=_('Countable plural forms for "answer"'),
        default=_('回答\n回答'),
        description=_('“回答”的可数名词复数'),
        help_text=_('Enter one form per line, pay attention'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_SINGULAR',
        #default=_('question'),
        #description=_('question (noun, singular)'),
        default=_('问题'),
        description=_('问题 (名词, 单数)'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED_QUESTION_SINGULAR',
        # lxw
        # default=_('unanswered question'),
        # description=_('unanswered question (singular)'),
        default=_('未回答的问题'),
        description=_('未回答的问题（单数）'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED_QUESTION_PLURAL',
        # lxw
        # default=_('unanswered questions'),
        # description=_('unanswered questions (plural)'),
        default=_('未回答的问题'),
        description=_('未回答的问题（复数）'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_SINGULAR',
        # 回答
        # default=_('answer'),
        # description=_('answer (noun, singular)'),
        default=_('回答'),
        description=_('回答（单数）'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_VOTED_UP',
        #default=_('Question voted up'),
        #description=_('Question voted up'),
        default=_('问题投票'),
        description=_('问题投票'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_VOTED_UP',
        #default=_('Answer voted up'),
        #description=_('Answer voted up'),
        default=_('回答投票'),
        description=_('回答投票'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NICE_ANSWER',
        #default=_('Nice Answer'),
        #description=_('Nice Answer'),
        default=_('优秀回答'),
        description=_('优秀回答'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NICE_QUESTION',
        #default=_('Nice Question'),
        #description=_('Nice Question'),
        default=_('精细问题'),
        description=_('精细问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GOOD_ANSWER',
        #default=_('Good Answer'),
        #description=_('Good Answer'),
        default=_('好的回答'),
        description=_('好的回答'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GOOD_QUESTION',
        default=_('Good Question'),
        description=_('Good Question'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GREAT_ANSWER',
        #default=_('Great Answer'),
        #description=_('Great Answer'),
        default=_('优秀回答'),
        description=_('优秀回答'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GREAT_QUESTION',
        default=_('优秀问题'),
        description=_('优秀问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_POPULAR_QUESTION',
        #default=_('Popular Question'),
        #description=_('Popular Question'),
        default=_('大众问题'),
        description=_('大众问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_NOTABLE_QUESTION',
        #default=_('Notable Question'),
        #description=_('Notable Question'),
        default=_('显著问题'),
        description=_('显著问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FAMOUS_QUESTION',
        #default=_('Famous Question'),
        #description=_('Famous Question'),
        default=_('出名问题'),
        description=_('出名问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_STELLAR_QUESTION',
        #default=_('Stellar Question'),
        #description=_('Stellar Question'),
        default=_('主要问题'),
        description=_('主要问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FAVORITE_QUESTION',
        #default=_('Favorite Question'),
        #description=_('Favorite Question'),
        default=_('受喜爱的问题'),
        description=_('受喜爱的问题'),
        help_text=_('Badge name'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_SHOW_ONLY_QUESTIONS_FROM',
        #default=_('Show only questions from'),
        #description=_('Show only questions from'),
        default=_('仅显示问题来源'),
        description=_('仅显示问题来源'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_ASK_YOUR_QUESTION_HERE',
        #default=_('Please ask your question here'),
        #description=_('Please ask your question here'),
        default=_('在此处提问'),
        description=_('在此处提问'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_PLEASE_ENTER_YOUR_QUESTION',
        #default=_('Please enter your question'),
        #description=_('Please enter your question'),
        default=_('请输入问题'),
        description=_('请输入问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ASK_A_QUESTION_INTERESTING_TO_THIS_COMMUNITY',
        #default=_('Ask a question interesting to this community'),
        #description=_('Ask a question interesting to this community'),
        default=_('问该社区有意思的问题'),
        description=_('问该社区有意思的问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REPOST_AS_A_QUESTION_COMMENT',
        #default=_('repost as a question comment'),
        #description=_(repost as a question comment),
        default=_('重新发布问题评论'),
        description=_('重新发布问题评论'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ONLY_ONE_ANSWER_PER_USER_IS_ALLOWED',
        #default=_('(Only one answer per user is allowed)'),
        #description=_('Only one answer per user is allowed'),
        default=_('(每个用户只允许作一个回答)'),
        description=_('每个用户只允许作一个回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_BEST_ANSWERS_FOR_YOUR_QUESTIONS',
        #default=_('Accept best answers for your questions'),
        #description=_('Accept best answers for your questions'),
        default=_('接受对你的问题最好回答'),
        description=_('接受对你的问题最好回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_AUTHOR_OF_THE_QUESTION',
        # lxw
        # default=_('author of the question'),
        # description=_('author of the question'),
        default=_('问题提出者'),
        description=_('问题提出者'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_OR_UNACCEPT_THE_BEST_ANSWER',
        #default=_('accept or unaccept the best answer'),
        #description=_('accept or unaccept the best answer'),
        default=_('是否接受该最好回答'),
        description=_('是否接受该最好回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ACCEPT_OR_UNACCEPT_OWN_ANSWER',
        #default=_('accept or unaccept your own answer'),
        #description=_('accept or unaccept your own answer'),
        default=_('是否接受你个人回答'),
        description=_('是否接受你个人回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOU_ALREADY_GAVE_AN_ANSWER',
        #default=_('you already gave an answer'),
        #description=_('you already gave an answer'),
        default=_('你已经给过回答'),
        description=_('你已经给过回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWER_OWN_QUESTIONS',
        # lxw
        # default=_('answer own questions'),
        # description=_('answer own questions'),
        default=_('回答自己的问题'),
        description=_('回答自己的问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED_OWN_QUESTION',
        # lxw
        # default=_('Answered own question'),
        # description=_('Answered own question'),
        default=_('已回答的自己的问题'),
        description=_('已回答的自己的问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REPOST_AS_A_COMMENT_UNDER_THE_OLDER_ANSWER',
        #default=_('repost as a comment under older answer'),
        #description=_('repost as a comment under older answer'),
        default=_('对之前回答重新发表评论'),
        description=_('对之前回答重新发表评论'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_INVITE_OTHERS_TO_HELP_ANSWER_THIS_QUESTION',
        # lxw
        # default=_('invite other to help answer this question'),
        # description=_('invite other to help answer this question'),
        default=_('邀请其他人回答该问题'),
        description=_('邀请其他人回答该问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RELATED_QUESTIONS',
        # lxw
        # default=_('Related questions'),
        # description=_('Related questions'),
        default=_('相关问题'),
        description=_('相关问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_TOOLS',
        # lxw
        # default=_('Question Tools'),
        # description=_('Question Tools'),
        default=_('问题工具'),
        description=_('问题工具'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THIS_QUESTION_IS_CURRENTLY_SHARED_ONLY_WITH',
        #default=_('Phrase: this question is currently shared only with:'),
        #description=_('Phrase: this question is currently shared only with:'),
        default=_('该问题只能由以下方式分享'),
        description=_('该问题只能由以下方式分享'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_BE_THE_FIRST_TO_ANSWER_THIS_QUESTION',
        #default=_('Be the first one to answer this question!'),
        #description=_('Be the first one to answer this question!'),
        default=_('第一个回答该问题'),
        description=_('第一个回答该问题'),             
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FOLLOW_QUESTIONS',
        # lxw
        # default=_('follow questions'),
        # description=_('follow questions'),
        default=_('关注问题'),
        description=_('关注问题'),
        help_text=_('Verb in the infinitive form'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_FOLLOWED_QUESTIONS',
        # lxw
        # default=_('followed questions'),
        # description=_('followed questions'),
        default=_('关注的问题'),
        description=_('关注的问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOU_CAN_POST_QUESTIONS_BY_EMAILING_THEM_AT',
        #default=_('You can post questions by emailing them at'),
        #description=_('You can post questions by emailing them at'),
        default=_('你可以发邮件发布问题'),
        description=_('你可以发邮件发布问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_LIST_OF_QUESTIONS',
        # lxw
        # default=_('List of questions'),
        # description=_('List of questions'),
        default=_('问题列表'),
        description=_('问题列表'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_COMMUNITY_GIVES_YOU_AWARDS',
        #default=_('Community gives you awards for your questions, answers and votes'),
        #description=_('Community gives you awards for your questions, answers and votes'),
        default=_('社区会对你发布的问题、回答和投票给予奖励'),
        description=_('社区会对你发布的问题、回答和投票给予奖励'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_CLOSE_QUESTION',
        # lxw
        # default=_('Close question'),
        # description=_('Close question'),
        default=_('关闭问题'),
        description=_('关闭问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_CLOSE_QUESTIONS',
        # lxw
        # default=_('close questions'),
        # description=_('close questions'),
        default=_('关闭问题'),
        description=_('关闭问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_QUESTION',
        # lxw
        # default=_('Edit question'),
        # description=_('Edit question'),
        default=_('编辑问题'),
        description=_('编辑问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_QUESTION_IN_ONE_SENTENCE',
        #default=_('Question - in one sentence'),
        #description=_('Question - in one sentence'),
        default=_('请用一句话描述问题'),
        description=_('请用一句话描述问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RETAG_QUESTION',
        #default=_('Retag question'),
        #description=_('Retag question'),
        default=_('问题重新标签'),
        description=_('问题重新标签'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_RETAG_QUESTIONS',
        #default=_('retag questions'),
        #description=_('retag questions'),
        default=_('问题重新标签'),
        description=_('问题重新标签'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_REOPEN_QUESTION',
        #default=_('Reopen question'),
        #description=_('Reopen question'),
        default=_('重新打开问题'),
        description=_('重新打开问题'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_THIS_ANSWER_HAS_BEEN_SELECTED_AS_CORRECT',
        #default=_('this answer has been selected as correct'),
        #description=_('this answer has been selected as correct'),
        default=_('该回答被选为正确回答'),
        description=_('该回答被选为正确回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_MARK_THIS_ANSWER_AS_CORRECT',
        #default=_('mark this answer as correct'),
        #description=_('mark this answer as correct'),
        default=_('把该回答标记为正确回答'),
        description=_('把该回答标记为正确回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_LOGIN_SIGNUP_TO_ANSWER',
        #default=_('Login/Signup to Answer'),
        #description=_('Login/Signup to Answer'),
        default=_('回答'),
        description=_('回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_YOUR_ANSWER',
        # lxw
        # default=_('Your Answer'),
        # description=_('Your Answer'),
        default=_('你的回答'),
        description=_('你的回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ADD_ANSWER',
        # lxw
        # default=_('Add Answer'),
        # description=_('Add Answer'),
        default=_('增加回答'),
        description=_('增加回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_GIVE_AN_ANSWER_INTERESTING_TO_THIS_COMMUNITY',
        #default=_('give an answer interesting to this community'),
        #description=_('give an answer interesting to this community'),
        default=_('给该社区有意思的回答'),
        description=_('给该社区有意思的回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_TRY_TO_GIVE_AN_ANSWER',
        #default=_('try to give an answer, rather than engage into a discussion'),
        #description=_('try to give an answer, rather than engage into a discussion'),
        default=_('尝试给一个回答而不是参与讨论'),
        description=_('尝试给一个回答而不是参与讨论'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_SHOW_ONLY_SELECTED_ANSWERS_TO_ENQUIRERS',
        #default=_('show only selected answers to enquirers'),
        #description=_('show only selected answers to enquirers'),
        default=_('仅展示被选出的回答给查询者'),
        description=_('仅展示被选出的回答给查询者'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_UNANSWERED',
        # lxw
        # default = _('UNANSWERED'),
        # description = _('UNANSWERED'),
        default = _('未回答'),
        description = _('未回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_EDIT_ANSWER',
        # lxw
        # default=_('Edit Answer'),
        # description=_('Edit Answer'),
        default=_('编辑回答'),
        description=_('编辑回答'),
        localized=True
    )
)

settings.register(
    values.StringValue(
        WORDS,
        'WORDS_ANSWERED',
        # lxw
        # default=_('Answered'),
        # description=_('Answered'),
        default=_('已回答'),
        description=_('已回答'),
        localized=True
    )
)