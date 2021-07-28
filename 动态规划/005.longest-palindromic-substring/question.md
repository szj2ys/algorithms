Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Example:

Input: "cbbd"

Output: "bb"

## [分析](https://leetcode-cn.com/problems/longest-palindromic-substring/solution/5-zui-chang-hui-wen-zi-chuan-dong-tai-gu-p7uk/)
    
动态规划：填dp表、当前ij状态、过去ij状态、如何联合得到输出、边界条件

定义状态：题目让我们求什么，就把什么设置为状态
题目求s中最长的回文子串，那就判断所有子串是否为回文子串，选出最长的
因此：dp[i][j]表示s[i:j+1]是否为回文子串（这里+1是为了构造闭区间）

状态转移方程：对空间进行分类讨论（当前ij状态、过去ij状态 如何联合得到输出）
当前ij状态：头尾必须相等（s[i]==s[j]）
过去ij状态：去掉头尾之后还是一个回文（dp[i+1][j-1] is True）
边界条件：只要是找过去ij状态的时候，就会涉及边界条件（即超出边界情况处理）
当i==j时一定是回文
j-1-(i+1)<=0,即j-i<=2时，只要当s[i]==s[j]时就是回文，不用判断dp[i+1][j-1]
dp[i][j] 为截取的子串

初始状态：这里已经直接判断j-i<=2的情况了，因此用不到初始状态，可以不设

输出内容：每次发现新回文都比较一下长度，记录i与长度

优化空间提速



