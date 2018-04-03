# PandasProject1
## 利用pandas对医院相关字段进行去重合并操作
>Hi
       附近是一个来自于不同数据源的医院列表， 里面包含重复医院， 需要把重复的医院合并。  
       判断2个医院重复的依据    NAME/  All_Alias 两列。     All_Alias 包含很多  alias，  都用   ###， 首先 你要获得 一行里面   name / alias  所有名称组成的   名字组，
 再通过2个医院的名字组是否重合， 判断2家医院是否为同一个医院 （有一个相同即为相同）


       信息整合规则 
                需要合并的信息是   【All_Alias,   CODE,   SOURCE】   ， 用 ###合并， 注意合并前要去重

                其他列保留的优先级为：
                卫计委>MOH>CPA>Mundi>Merck>挂号>Pfizer>haodf)

       要求
                python  2.7  编写
                1.   代码整洁， 易读取
                2.   尽量使用标准 python 库， 例如 pandas
                3.   注意程序效率

