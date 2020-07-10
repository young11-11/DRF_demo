from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    """图书序列化器类"""
    id = serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期')
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    # 关联对象嵌套序列化字段
    # heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    # heroinfo_set = serializers.StringRelatedField(label='英雄', many=True)
    # heroinfo_set = HeroInfoSerializer(label='英雄', many=True)

    def validate_btitle(self, value):
        """此方法针对btitle字段的内容进行补充验证"""

        if 'django' not in value.lower():
            raise serializers.ValidationError("图书不是关于Django的-2")

            # 注意：必须返回值！！！
        return value


class HeroInfoSerializer(serializers.Serializer):
    """英雄序列化器类"""
    GENDER_CHOICES = (
        (0, '男'),
        (1, '女')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(label='性别', choices=GENDER_CHOICES, required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False)
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', read_only=True)
    # hbook = BookInfoSerializer(label='图书')
    hbook = serializers.StringRelatedField(label='图书')
