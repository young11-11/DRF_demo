from IPython.utils.coloransi import value
from rest_framework import serializers

from booktest.models import BookInfo


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

    # def validate(self, attrs):
    #     btitle = attrs.get('btitle')
    #
    #     if 'django' not in value.lower():
    #         raise serializers.ValidationError("图书不是关于Django的-3")
    #
    #     # 注意：必须返回值！！！
    #     return attrs

    def create(self, validated_data):
        """
        validated_data：校验之后的数据
        """
        # 利用校验之后的数据，来向数据库中添加图书
        book = BookInfo.objects.create(**validated_data)
        # 返回book对象
        return book

    def update(self, instance, validated_data):
        """
        instance: 创建序列化器对象时，传入的实例对象
        validated_data: 校验之后的数据
        """
        # 需求：利用校验之后的数据，对instance数据进行更新
        btitle = validated_data.get('btitle')
        bpub_date = validated_data.get('bpub_date')
        bread = validated_data.get('bread')
        bcomment = validated_data.get('bcomment')

        # 更新
        instance.btitle = btitle
        instance.bpub_date = bpub_date
        instance.bread = bread
        instance.bcomment = bcomment
        # 调用模型对象的save，实现数据库中数据更新
        instance.save()

        # 返回对象
        return instance



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
