# coding:gbk
import numpy


class MineData:
    '''
    ����˵����
        size: ������С
        mineSum: �׵�����
        minefieldsType: ����״̬
            none: δ֪/δ�㿪
            mine: ʧ��ʱδ���е���
            mine_dead: ʧ��ʱ���е���
            mine_wrong: ʧ��ʱ��Ǵ���ļ���
            flag: ���׵ı��
            '012345678': ��ʾ��Χ��������
        minefieldsStatus: ��Ϸ������״̬��Flase��ʾΪ�ѱ�ǵ��ڲ���True��ʾ�ѱ�ǵı�Ե��δ�������
    '''
    size = (8, 8)
    mineSum = 10
    minefieldsType = []
    minefieldsStatus = []
    probability = None
    status = None

    def __init__(self, size=(8, 8), mineSum=10):
        MineData.size = size
        MineData.mineSum = mineSum
        MineData.minefieldsType = [['none'] * size[1] for i in xrange(size[0])]
        MineData.minefieldsStatus = [[True] * size[1] for i in xrange(size[0])]
        MineData.probability = numpy.zeros(size)
