# 理解了namedtuple函数的参数，我们就可以创建具名元组了
# >>> Point = namedtuple('Point', ['x', 'y'])  # 返回一个名为`Point`的类，并赋值给名为`Point`的变量
# >>> p = Point(11, y=22)     # 可以根据参数的位置，或具名参数来实例化（像普通的类一样）
# >>> p[0] + p[1]             # 具名元组可以像普通元组一样通过`index`访问
# 33
# >>> x, y = p                # 具名元组可以像普通元组一样解包
# >>> x, y
# (11, 22)
# >>> p.x + p.y               # 具名元组还可以通过属性名称访问元组内容
# 33
# >>> p                       # 具名元组在调用`__repr__`,打印实例时，更具可读性
# Point(x=11, y=22)
#
# 作者：天边一钩残月带三星
# 链接：https://www.jianshu.com/p/60e6484a7088
# 来源：简书
# 简书著作权归作者所有，任何形式的转载都请联系作者获得授权并注明出处。


from random import choice
import collections
Card =collections.namedtuple('Card',['rank','suit'])
class FrenchDeck:
    ranks =[str(n) for n in range(2,11)]+list('JQKA')
    print(ranks)
    suits='spades diamonds clubs herts'.split()
    print(suits)
    def __init__(self):
        self._cards=[Card(rank,suit) for suit in self.suits for rank in self.ranks ]
        print(self._cards)
    def __len__(self):
        return len(self._cards)
    def __getitem__(self,position):
        return self._cards[position]
deck = FrenchDeck()


print(len(deck))
print(choice(deck))
for card in deck:
    print(card)