# 力扣(leetcode)编辑器

我不生产题，我只是力扣运行环境的搬运工。

项目地址：https://github.com/boristown/lceditor

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


  5. 完整代码请参考[常规题示例](sample1.py)和[设计题示例](sample2.py)。

  6. 结合Github Copilot插件使用，体验更佳：

![lceditor+copilot自动刷题](/pics/lceditor_copilot.gif)

[lceditor+copilot自动刷题.mp4](/pics/lceditor_copilot.mp4)