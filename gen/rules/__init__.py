from .search_replace import SearchReplace
from .search_replace.rule_change_accent import RuleChangeAccent
from .search_replace.rule_prefix import RulePrefix
from .search_replace.rule_remove_accent import RuleRemoveAccent
from .search_replace.rule_suffix import RuleSuffix
from .search_replace.rule_telex import RuleTelex
from .search_replace.rule_vni import RuleVni

search_replace = SearchReplace([
    # RuleTelex,
    # RuleVni,
    RulePrefix,
    RuleSuffix,
    RuleChangeAccent,
    RuleRemoveAccent
])
