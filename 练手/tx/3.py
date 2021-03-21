

# 可以自定义比较函数，决定排序方式
def cmp(a,b):
    return a>b


class quiteSort:
    def __init__(self):
        self.cmp = lambda a, b:a< b

    # 设置比较函数
    def setCmp(self, cmp):
        self.cmp =cmp

    # 随机找一个中间基准值，将数据分成左右两堆
    def randomized_partition(self, nums, l, r):
        import random
        pivot = random.randint(l, r)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        i = l - 1
        for j in range(l, r):
            if self.cmp(nums[j],nums[r]):
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
        i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    # 不断进行细分
    def randomized_quicksort(self, nums, l, r):
        if r - l <= 0:
            return
        mid = self.randomized_partition(nums, l, r)
        self.randomized_quicksort(nums, l, mid - 1)
        self.randomized_quicksort(nums, mid + 1, r)

    def sortArray(self, nums):
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums


class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # 计算每一段的替换结果，因为不会重叠，就直接分段
        def cal(s, source, target):
            # print(s, target, source)
            if s[0: len(source)] == source:
                s = target + s[len(source): len(s)+1]
            # print(s)


            return s


        meta = []
        for i in range(len(indexes)):
            meta.append([indexes[i], sources[i], targets[i] ])

        meta = sorted(meta)
        ans = ''

        segments = []
        if meta[0][0]  != 0:
            ans+= S[0: meta[0][0]]
            # segments.append(S[0: indexes[0]])
        for i in range(len(indexes) -1):
            left = meta[i][0]
            right =meta[i+1][0]
            print(left, right)
            segments.append(S[left: right])


        segments.append(S[meta[-1][0] : len(S) +1] )

        print(segments)

        length = len(segments)

        for i in range(length):
            ans += cal(segments[i] , meta[i][1], meta[i][2])

        print(ans)
        # print("fffoapglhmwyzglqeujkogpniunvsvmfzhaaxrztcxrpazxslfefaemeegltolydhnqqpqjhuqlafsjignvcrnrxctymkmmfveunnoentunxxwxdxooxfwhfewnebmnqleglqnbxaebmqxluoaxzrtiqnlesfvstntdewpvlhrtwgtjmwticbddiutqayqplckzoyfnapskxckhbqblvtyocqwdaxirvigrdndssuveompqkemtbwrsmpdqwsfpvyyqbvyedpreiezuntuyjqshkejttfkcjaxyhtdwmzsllqucxzcorlrxtgrxydezlzbpaddqqkjpfucyucewelchskdmmikscciegzoijywgtkjmnzyxeygiourgumfpffogjkhobmhwtahwyhyxwcmusvhikofbnhhcawcvzaykyashchyeycijceagvkdttatmrkmrfspphdivrwywtlxebwtquvenjazsvvrehcqyxpdmliqjybxhtycmlybhxvesolsbykuhwphhvuccwjoddxtrurbetdahykxmlhkxhvovhccyxfsxmcuhiiiewcluehelobjqzpigdxmjitwkdfbgmoggvlvmmljtxvrbjngrubndiexsjghpuseawrbkhvjnavrzmxxvrkmbvyvvizpcawscooerpdsmbjpjmwkhovkcqzbhygemwhfltviwhytgmjzsroqljbiguvtwwyupbxhcmgutriibbticcscmeariwyrukefziegopjbskurqqrcujjjlxbndbaysbhyulqwncpdziozhocerwvalltmbsfvxztomobwbyvphjmvauahxszyjivtxauquxjmifixbdjiymfkjfmwdgscepybwdjojjkknwdobuepsptwsvwgznetyzlddfwxobnzgfoylrqzayzfbnqjiuhkalukuvosohjdjxjtrygzdgvxqcbxbgvooqfxqjurvmukisnhhagfjpkbq")
        return ans






Solution.findReplaceString(None,"fffoapgrfucxusxhcvbblanunvsvmfzhaaxrztcnucdpiuhnodomeegltolyvaoqqpqjhuqlafsjignmrnffafvngwamfveuncfvmvnxxwxdxosnohfwybxdfmwnalqnbxaevrrmyoaxzrnjhywyfvstndsewnllhrtwsvxenkscbivijfqnysamckzoyfnapuotmdexzkkrpmppttficzerdndssuveompqkemtbwbodrhwsfpbmkafpwyedpcowruntvymxtyyejqtajkcjakghtdwmuygecjncxzcxezgecrxonnszmqmecgvqqkdagvaaucewelchsmebikscciegzoiamovdojrmmwgbxeygibxxltemfgpogjkhobmhwquizuwvhfaiavsxhiknysdghcawcrphaykyashchyomklvghkyabxatmrkmrfsppfhgrwywtlxebgzmevefcqquvhvgounldxkdzndwybxhtycmlybhaaqvodntsvfhwcuhvuccwcsxelafyzushjhfyklvghpfvknprfouevsxmcuhiiiewcluehpmzrjzffnrptwbuhnyahrbzqvirvmffbxvrmynfcnupnukayjghpusewdwrbkhvjnveuiionefmnfxaowjzzonyfcprboojihghhjfnithovkpfgbhyqxqenyrhmfljqxpopzpfjroqligbigudoqpunaxqyjpkjriibbticcscmearhnwhlxfajbcegopeqskurqqruhqyzpdntwfaemcnopsypyqcpwaexzhocerwvallzqhyidvmnmaobkmbzsxfabkmgqouquxchuxjmimqbxbdjuokeinjzionekaygnoiyytjkvgwdobuepmbtwsvwhwkephlddfwxobnlobfhadrqbtlzzownleiuhkalupfjosfkjiuagxjgudzqqqnwqcxbgvooqfxqjurybcuufsnhxpifjpkbxpztffxhj",
[613,655,717,636,211,833,746,462,20,430,680,694,686,817,659,261,978,79,626,996,115,254,193,606,795,374,181,522,895,924,501,548,404,414,334,761,132,234,285,577,82,936,7,487,828,164,470,672,304,974,810,97,711,888,296,157,609,770,539,60,899,617,204,264,366,319,841,110,910,983,39,571,665,348,142,450,153,991,855,949,944,485,146,476,822,173,814,848,386,919,600,688,427,270,278,927,831,357,243,468],
["pnuk","onyf","doqpunaxqyjpkj","veuiionefmnfxaowjz","icze","mgqouqu","hnwhlxfajbc","gzme","lan","lvghkyabx","pfg","mfljqxpopzpfj","qx","mnma","cprb","vym","ufs","mr","wd","fx","wybxdfmwna","cowr","uotmdexzkkr","my","waex","gp","sam","csxelafyzushjhf","hwk","ow","aaqvodntsvfhwcu","prfouev","nysdg","rph","meb","eq","vrrmy","bodrh","uygecjn","ffnrptwbuhnyahrbzqvir","ffafvngwa","pfjosfk","rfucxusxhcvbb","dw","xf","svxenks","qquvhv","fnit","onnszmqmecgvq","ybc","zqhy","cfvmv","ig","mb","xezgec","nl","fcn","uhqyzpdntwfaemcnopsypyq","lvghpfvkn","vao","ph","ay","pmppttf","xtyy","bxxlte","dagvaa","ch","sno","lobfhad","xpi","nucdpiuhnodo","pmzrj","jihghh","amovdojr","njhy","fhg","ds","xpz","uokeinjzionekaygnoiyytjkvgw","jgudzqqqnwqc","iuagx","zn","wy","gounldxkd","bkmbzs","ivijfqn","id","mqb","quizuwvhfaiavsx","btlz","ffb","qenyrh","omk","qtaj","kg","le","bk","mwgb","bmkafpwy","fc"],
["bndi","pca","vtwwyupbxhcmgut","avrzmxxvrkmbvyvvi","irvig","xszyjivt","iwyrukefzi","wtqu","gpni","jceagvkdtt","cqz","tviwhytgmjzs","ge","xztom","wsc","uyj","kis","vcr","a","xbn","ewnebmnqleg","reiez","skxckhbqblvt","bj","dzio","pff","qpl","joddxtrurbetdah","gzn","fb","xvesolsbykuhwph","hccyxf","ofbnh","vz","kdmm","jb","bmqxlu","rsmpdq","zsllqu","pigdxmjitwkdfbgmoggvl","rxctymkm","kuvosoh","lhmwyzglqeujko","qj","jmv","gtjmwti","zsvvr","pjmwk","ydezlzbpaddq","vm","tmbs","noentu","j","sp","orlrxtg","pv","gr","cujjjlxbndbaysbhyulqwn","xmlhkxhvov","dhn","tyz","exs","yocqwdax","qshk","ourgu","jpfucy","auq","oxfw","zgfoyl","hag","xrpazxslfefae","elobjq","erpdsmb","jywgtkj","tiqnl","hdiv","td","qd","iymfkjfmwdgscepybwdjojjkknw","trygzdgvxqcb","djxj","li","es","ehcqyxpdm","bwbyvph","ddiutqa","f","fi","tahwyhyxwcmusv","zay","mljt","mwhfl","eyci","ttf","xy","qj","uah","nzy","vyyqbvy","nja"]



                           )


"vbfrssozp"