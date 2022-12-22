# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def fn(node, lo, hi):                       # Дополнительная функция, которая будет вызываться рекурсивно
            if not node: return hi - lo             # Если есть вершина: Возвращаем разность наименьшего и наибольшего значения
            left = fn(node.left, lo, node.val)      # В левой ветви вызываем рекурсию, где в качестве вершины берем вершину левой ветви, наименьшее значение оставляем, наибольшим указываем основную вершину
            right = fn(node.right, node.val, hi)    # Сооветствующую рекурсию вызываем и на правой ветви.
            return min(left, right)                 # Возвращаем минимальное значение из двух возможных

        return fn(root, float('-inf'), float('inf')) #Возвращаем результат вызова рекурсивной функции, со значениями бесконечности.