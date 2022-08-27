# 力扣(leetcode)编辑器

完美复制力扣Python3运行环境，

> 需要python3.10以上环境

> 以下教程通过Visual Studio Code演示
  
  ## 使用方式：

  1. 引入lclibs和lceditor：

  ```Python
 from lclibs import *
 import lceditor
  ```

  2. 编写力扣解决方案代码：
     
  ```Python
  # 1. 两数之和
  # https://leetcode.cn/problems/two-sum/
  class Solution:
      def twoSum(self, nums: List[int], target: int) -> List[int]:
          n = len(nums)
          for i in range(n):
              for j in range(i + 1, n):
                  if nums[i] + nums[j] == target:
                      return [i, j]
          return []
  ```

  3. 调用lceditor.run,并传入输入文件路径:

  ```Python
  if __name__ == '__main__':
      lceditor.run("sample1.txt")
  ```

  4. 执行/调试。
    
- 常规题：

![常规题](/pics/sample1.jpg)

- 设计题：

![设计题](/pics/sample2.jpg)


  5. 完整代码请参考`samply1.py`和`sample2.py`。