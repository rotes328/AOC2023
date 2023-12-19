import json

class Rule:
    def __init__(self, letter, operation, value, next_rule):
        self.letter = letter
        self.operation = operation
        self.value = int(value)
        self.next_rule = next_rule


class RuleSet:
    def __init__(self, rule_text):
        self.rule_text = rule_text
        self._parse()

    def __repr__(self) -> str:
        return str(self.rule_text)

    def _parse(self):
        self.conditions = []
        for test in self.rule_text.split(','):
            if len(test) > 1 and test[1] in {'<', '>'}:
                self.conditions.append(Rule(test[0], test[1], *test[2:].split(":", 1)))
            else:
                self.conditions.append(test)


    def evaluate(self, part):
        for test in self.conditions:
            if isinstance(test, str):
                return test
            elif test.operation == '>':
                if part[test.letter] > test.value:
                    return test.next_rule
                else:
                    continue
            elif test.operation == '<':
                if part[test.letter] < test.value:
                    return test.next_rule
                else:
                    continue


def get_rules():
    rules_instances = {}

    with open('rules.txt', 'r', encoding='UTF-8') as data:
        for line in data.read().splitlines():
            class_name, rule_text = line.split('{', 1)
            class_name = class_name.strip()
            rule_instance = RuleSet(rule_text.rstrip('}'))
            rules_instances[class_name] = rule_instance
    return rules_instances


def main():
    rules_instances = get_rules()

    with open('data.txt', 'r', encoding='UTF-8') as data:
        total = 0
        for line in data.read().splitlines():
            json_format_string = line.replace('=', '":').replace('{', '{"').replace(',', ',"').replace('}', '}')
            part = json.loads(json_format_string)
            test = "in"
            while test not in ['A', 'R']:
                test = rules_instances[test].evaluate(part)
                if test == 'A':
                    total += sum(part.values())

    print('Part 1 Answer: ', total)


if __name__ == '__main__':
    main()
