##推荐系统##

**数据集：**一个数据集合通常包含用户，商品，评价三个部分。用户和商品是数据集的两个维度，而评价把两者联系起来。

**用户相似度：**对相同商品的评价相似的用户是相似的

**商品相似度：**

**euclid distance**

**pearson relation**

**tanimoto similarity** which is a generalization of Jaccard coefficient. it is the ratio the size of intersection of two sets to the size of their union.

**曼哈顿距离：**在欧几里德空间的固定直角坐标系上两点所形成的线段对轴产生的投影的距离总和。
                           `d(i,j)=|x1-x2|+|y1-y2|`

**推荐系统：**向用户提供用户想买的商品。用户为目标，商品为内容。通常分为两种，一种基于用户的推荐，一种是基于商品的推荐。

已知：用户及其所需要的商品
结果：用户

**基于用户的协作型过滤（user-based collaborative filtering）：**已知一个用户，向其推荐商品

	1.根据用户的历史数据，在数据集中查找到同样购买相似商品的其他用户
	2.根据其他用户的评价，得到相似的用户
	3.
	

**基于商品的协作型过滤（item-based collaborative filtering）：**已知一个商品，推荐类似商品，

总体思路:

    1.为每件物品计预先计算好最为相似的其他物品
    2.从某一用户曾经评价过的物品中，选出排位靠前者，构造加权列表，其中包含了与这些选中物品最为相似的其他物品。

优势：

- 需要拥有大量的数据
- 允许大量计算任务预先执行：物品间的比较不像用户间的比较那么频繁变化，并且随着用户的增长，物品间的相似度区域稳定


## 欢迎使用 MarkdownPad 2 ##

**MarkdownPad** 是 Windows 平台上一个功能完善的 Markdown 编辑器。

### 专为 Markdown 打造 ###

提供了语法高亮和方便的快捷键功能，给您最好的 Markdown 编写体验。

来试一下：

- **粗体** (`Ctrl+B`) and *斜体* (`Ctrl+I`)
- 引用 (`Ctrl+Q`)
- 代码块 (`Ctrl+K`)
- 标题 1, 2, 3 (`Ctrl+1`, `Ctrl+2`, `Ctrl+3`)
- 列表 (`Ctrl+U` and `Ctrl+Shift+O`)

### 实时预览，所见即所得 ###

无需猜测您的 [语法](http://markdownpad.com) 是否正确；每当您敲击键盘，实时预览功能都会立刻准确呈现出文档的显示效果。

### 自由定制 ###
 
100% 可自定义的字体、配色、布局和样式，让您可以将 MarkdownPad 配置的得心应手。

### 为高级用户而设计的稳定的 Markdown 编辑器 ###
 
 MarkdownPad 支持多种 Markdown 解析引擎，包括 标准 Markdown 、 Markdown 扩展 (包括表格支持) 以及 GitHub 风格 Markdown 。
 
 有了标签式多文档界面、PDF 导出、内置的图片上传工具、会话管理、拼写检查、自动保存、语法高亮以及内置的 CSS 管理器，您可以随心所欲地使用 MarkdownPad。
