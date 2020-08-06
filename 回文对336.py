# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:04:14 2020

@author: 53013
"""
'''
import time

class Solution:
    def palindromePairs(self, words):
        def ispalindrome(self,s):
            left = 0
            right = len(s)-1
            sub = s[left:right+1]
            return sub == sub[::-1]
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j or words[i][0] != words[j][-1]:
                    continue
                s = words[i] + words[j]
                if ispalindrome(self, s):
                    ans.append([i,j])
        return ans

'''
class Node:
    def __init__(self):
        self.ch = [0] * 26
        self.flag = -1


class Solution:
    def palindromePairs(self, words: list) -> list:
        tree = [Node()]

        def insert(s: str, index: int):
            length = len(s)
            add = 0
            for i in range(length):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    tree.append(Node())
                    tree[add].ch[x] = len(tree) - 1
                add = tree[add].ch[x]
            tree[add].flag = index

        def findWord(s: str, left: int, right: int) -> int:
            add = 0
            for i in range(right, left - 1, -1):
                x = ord(s[i]) - ord("a")
                if tree[add].ch[x] == 0:
                    return -1
                add = tree[add].ch[x]
            return tree[add].flag

        def isPalindrome(s: str, left: int, right: int) -> bool:
            length = right - left + 1
            return length < 0 or all(s[left + i] == s[right - i] for i in range(length // 2))

        n = len(words)
        for i, word in enumerate(words):
            insert(word, i)

        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret
    
class Solution:
    def palindromePairs(self, words):

        def findWord(s: str, left: int, right: int) -> int:
            return indices.get(s[left:right+1], -1)
        
        def isPalindrome(s: str, left: int, right: int) -> bool:
            sub = s[left:right+1]
            return (sub) == sub[::-1]
        
        n = len(words)
        indices = {word[::-1]: i for i, word in enumerate(words)}
        
        ret = list()
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                if isPalindrome(word, j, m - 1):
                    leftId = findWord(word, 0, j - 1)
                    if leftId != -1 and leftId != i:
                        ret.append([i, leftId])
                if j and isPalindrome(word, 0, j - 1):
                    rightId = findWord(word, j, m - 1)
                    if rightId != -1 and rightId != i:
                        ret.append([rightId, i])

        return ret
words = ["ajeceehad","dcbabigiaa","eedfaedg","bhcbhiahcj","d","jea","f","gejdhfjc","jgffdfcheicij","gjjdjdgbggdid","gjjfbidbji","ecafaieifcafihachfja","bbjgieab","afac","hfiacihhfhge","cdddhggj","ijhah","dcehhdiacjff","caaiedfachehejhgbca","dai","j","ichfbfbhgjjgddi","ddgjfgfigaii","fciag","bahehaaebdbcdbhdagef","hegaac","feich","h","ajjcegdhfijidaddajd","e","jidfihigdfjd","aggcbbdaefi","a","ihijidiibh","fdibjbd","fjcgajjegdaa","cif","bjfdace","dfiadcbijageeggaia","achihfjjjjja","djcgfdfbidbdjcb","fbbedjdc","dfgeheaiehiicbccie","bigffadhigchhi","ahhbiehcechfhbh","ijeecjdjadec","efcihddhgehib","fg","gdjihdjdh","bhhhbdgia","eheed","hfbeedaddebaihij","efeaadgehbbcjggdg","jijedcjchdd","beecahieedjgdfah","ac","hhaceideiecc","fhdegdaihgggae","hbcgacgch","c","cciacacjfgeiicfdgbj","bibafdd","fgghebddadcidf","hjcjiaifgjijfaefcebj","cehjbeibiedibbjgd","cidhbggid","dfgbfhej","jhaaaccg","cfbdgcjbfieeejhghe","daghagbiadcjidijbjj","gffejecabdeebhi","hgcihbae","abe","ejfabghjigag","ehiihfghbega","dhefahfadjfh","hdgbcbiedfiafiifgae","hihccgfabafch","ajdihajgbgaejgii","fadjbgjbggcjefhhd","ajhdgebhdcahcfje","jejcchiicce","eh","hca","acjecdabcdhiii","aefbbcagh","jfebecehdjhaeigbabb","jbbdfcahfjgggibbif","dibeidiifdecd","cbefbgbddebjbgfibdg","haggfciejcgaaghggigf","iid","cjbefghijcebdjhaaahh","eggebcfaeadjhdgacca","dhibbfhjgj","eifaheccjcjihgjgdcce","bfhdbgbia","hieajbbfbedcejjh","b","iejigifdcebi","jabhe","cbhdgbfbcfe","dhbjjhhbgfgbicd","jfb","fagabhigjiifihedge","jdbceejcbddfa","da","jach","jcbbfdgccfdi","ifh","ejibfdcggihddj","gj","agj","badhcgaifbhf","gfbafgei","ehdfceeejdie","jfaig","i","hfigidhaifagggfdfh","hbag","afc","jacghacfbhaccadg","hcafigeihicjef","fbcdeijjcjjagc","ebhgeajdcfecciefja","adcg","bjaecfgfeg","efj","jghcccbhfchccja","hbh","jjjcdjjgg","ggabc","dabadjecaehe","fejbihdgibfdidghdabc","ccgcbjch","jcb","hghcf","aaebgceehdcbgedjdgh","ecgabgecjfgagbb","dbfccdhfchibbfjdce","hajdeahjggbeidea","cfaicfgjeggjaabdiiji","dcbhieafbbeej","iicdgfjadbbj","dabdbcjbfccadebbfbf","hhgbgehggdddhcfhfggh","hbghfhjdeideh","jdffejf","aaajgfcgdcc","ghcggfj","eifif","eaidgdbhfjihjag","bigfccbfegaahchc","hbfgdbafh","abbdagae","bebejdfgjecfbebcgia","ccejibdbfbae","djbicdfdeaa","je","fhbgdhbehbdiecca","hgg","iebec","fgdh","gdgijefdhjdd","jbbigggjcdjcaig","gagehabedbij","fggacdhjghg","jcbagghdchd","dce","fd","gijacfggaeacebdefda","bcahbeefcgbiaeb","hfbjjcjcdbcddgacbgjc","ebbbijggjhiajcgej","agjehh","didcehggeeihiheij","bjcjjdiebceej","bgggacjf","dcjcbhhfiifgcga","ifdedi","idafddidfidfd","cgcfebcjjaddce","jhceiedadbaeadhd","jbbb","biajejfdbbej","fdgjed","ebaddiajedjhccjbeg","jbfjhjdjgfdgcdjcgd","ifeiheeiejhh","dcfhjdejiijcddfcfdj","bjcdac","fijfhadgfjaefb","acci","fhbajibajjhfjia","gec","habbjciadgde","gdgjca","hgcfaadgjgeeiej","cgbgefhdabgfihjbbbh","hcbhahbaajhehad","cdiaehdhdjia","fagajeab","ieiagbcchfie","djhgc","bhfc","af","gedeb","ea","gfb","dejcfcdicb","acfiidbi","bgahjbgaeag","gjiec","ccjdecefbjhcajfeda","gffdcihfahhachdei","cdbcjefffhddafaaf","fbjhbaaefhedfhbhbadd","efejf","bdhcgih","gicggeacd","ecfhijeja","fcjeehhcfeaj","gdhfjieigjbbcg","difhbhcbjdjaga","ieiggjffeadbcj","ddjbeahbadechf","gfdgjag","dggedhheijccegbgef","eieid","ibfhbh","gaaaidieaaghddgae","jbbcgfddaijeafjbf","haihdc","hfgicghi","cjjhiedj","dhicbefhaccgi","icgaaeiicdbabjda","cejbidcfajicjdfdf","hbaibehg","bgfddibjfdbfdcjjahb","ffeajcgjehcdcai","ecaabdgha","cbafajabgdficgcddddi","ffgdcjia","eaedhddaadbed","cedefhadffaaeihahbd","beieheaajiheafja","ibchda","afdhfdigeijcg","dgcfdbff","hedajbccdfdbghcaabd","bajijjecjehd","bjgffcfdh","eebjagefaededdg","ebiih","jhjaecdjgdfcjfga","bcihgehg","eahjaeibjgddcdhigcea","fcacdibieajcdagfhgg","bjhichdhc","jafgccceagaafhecggff","chdaggji","deahihdhbebhghbb","gdecbddecjccdjfcjj","jibiieeabadhjjcbfhca","hfacajajebf","hgijjfd","fdfjefgbiibbcagjd","ceebbdbb","jifbie","gdcdead","egajhgjijffhd","ihjbfgdhgidaeagdd","gh","ieeigbejfbhdf","ffifjbid","icgichhbhadjheahfhj","jgjijaidgehadbeicegd","bghhcecdiadgfa","ada","edgccg","abacgibgj","eijbeedicd","djddjahbfb","ec","jbbehabb","g","egcbicifgafdibeaedg","dhfchihhhggeacjiaegd","fiaeifeieahh","caieej","egjihj","feebacgcebhejh","gdaf","jja","gdcgef","jcajejihibe","dhabjiajfafijahhea","eceebicebjabbfhicib","gcd","aie","chffbbeaf","bjcacbbed","faidaihahbhhaegcd","bjgchbd","gjfhhijhcccadch","eeafbhg","jb","ajgdejbbcgjbaahif","iiccdhbdjabeabfceb","icedj","icjdgeeijcedhjgejcg","aaechbigd","if","bhbabdceifjg","jjdeeh","djjchbaa","jah","bjcacajdcdafcggfiee","fadieehghajdjhgbeicf","gbibgjccchghebhhhjh","ajfeejdbbha","iag","de","dhiegjdhaiadg","fajjgfccahabccffaf","hebfafabhg","gfhcggjdcbfdecdiiac","gcdbife","daeeaea","eijbegfajgafbafdbbbc","giib","efdhhbdgjdbacjcg","gegcbahdeedcdahdi","gbhehjdgcjeddefjhfhd","cai","igbaii","gcjaaaidhhdd","igib","cebfadbdffjfefggg","jajgaa","hbifjbjcbdaaaa","ibieheehdcchf","ahjiiifd","iifechfcc","gcaddd","egbadfjdidiegg","bfcbdcfhifgiagdhgbj","egf","cgagibegi","ffdejchjh","ibhfe","aaajicdedadhhceefg","ehjfajbibahgcdcagf","hadjfbb","jgfffhjcgcdcegbjcci","aahhhijibhgebiggd","bjbbeiggbbjddgjceb","ihcbigcaec","ge","efhhi","dgiifggeehcga","dachdh","cjagjcacdjbbiieafg","eddb","fehiaiieed","jedcfcbidaf","iffhheicgjdeia","hdbichbag","jcegebdihhfdbjaahi","badabffiic","gaad","dhadcbadiecacg","ceffbfhejbg","djgijcgciaijfh","bajcchfbhbijjeaahgjd","dia","jj","bcfdajh","gjfdifce","edehdfbfddic","bcajiihaffgigdfghbg","gecfacffj","cighaifb","jfeiiaheigjgdb","ifbb","jhjjefieefhgfehbcedb","cfaadbfbfadcbbjge","ecgajjgeii","jghjfibgefgigiiajc","ibdffjgffg","ciijebij","cdcjjficiaggi","geggaaae","bh","gdgifhfcehfjefieidf","fh","ijiibacjfgiaaffb","bbcedddhedgchjeeaeeg","dfgabeeb","bcddfehcbcbaifa","ihhfi","ffjja","jdfacibhfbhigffcca","fiaehhgibici","chhf","bbdeiaijjjbidjgi","difcaechihihchh","bj","dbfichafgjfcegdjhdb","fhfabdcahgjifgfdfg","chcdahjdfbffjeabcjd","bacicddcccbjjiaj","hhggjfgjdbfg","edcjegcc","fcdbcheh","gbjiieiiifjeegiiibc","gihccaagcaaadae","jdgciecahdcdegdeiaf","afheiabcdfji","gbibahbcad","ifgbhdahdffcfjigjj","aijeajigejdhdbdba","diiicefgbbefefaheeha","ceddfihfhccj","gg","dcgdbjbececfc","jhijhefabdcfhhh","gbhjdd","edehcjcjjh","acf","aijeiibdhadbhcgcgi","egfifechh","ebhid","chhcfceajacccc","ceeh","ghificfje","cgcfbiech","cgidhjde","bdddbghbfjdcjbdbd","bdhiciijfhf","hccjgbdjdehfg","gebabgdggeba","bhahghgaihdjhgdgb","dfehhhgcjiicacc","giac","hiaahecahcccfedjdb","ji","gfedcjci","hjghfhd","ahhcidfacaagg","gcggj","feebiijhabjibff","gacbihagagbfcgbce","cdaejhbdgfh","gjc","fbeebfi","cdbggfd","dhfchgih","chaiecdgfbhdj","cdhjjac","cfg","ejdggddfihhcagjidih","adabcahjejfdcfcf","dfchcbjheiedcicicj","jfigigjadaj","hfefhaagbabg","bcchechiajbcbf","hjjg","bicgeaghdjdgeibef","fee","hdacaddfg","fajaijhafifgibbghehj","ddi","gfhicijfdafhaghie","ijeicajdddjicdcdb","jgdfbefeeicgigfa","dhgehadh","bfgfjfg","hdieeecdifgbj","iji","gfadjjifjeijjcddac","cbbeiaegdgijbfegg","hbjbhf","egehjcgcadfjcdajhhd","fhjfcchhhfgcbfcefhc","hdaebabbeieb","feidhddhdi","jcja","cjifdfc","ejaieegdcijjjf","fejejch","icciegadgdcdefj","chgjidjbdjgc","fbbicccffa","iabaaafaic","jcjge","fhdfci","cegficjbbechcgjbjba","aajediecedgdjdgja","efecgdf","bbiehadi","bhgdafafiiai","ihgfajdjje","accebfjfhiefai","bcchdbac","dgeidc","fhhhhhbbi","hiejjefejbcjbcifhf","fdedfaddfcggahgdceeh","ibib","hai","cddgabgifj","fgaihfhiegbdie","iccdhfegf","cj","ieicgcighehbche","jaabcdidgdfj","hfcecgdjaffbchbidfe","jaajgdeaegda","hefiih","afcfgjbi","bbdabhhig","jeiieefbgdcfbj","ihg","jhijf","bbfddbd","dieafbcdeddfbghddfh","cdibicghjcdajfhiefcg","agfahcegbbgffhcfdi","gbafibbdbbaghi","ghfabddhe","jddhcjabaeccbcg","gacdahcg","eabgdjdcdhbed","chijdahdib","ehcbchcjhfjcgc","afciaafajdjfcccihd","bjedfjifccade","dajhddja","gihjggecejdegcjhcdfg","iahigcbi","gfahgdc","ghchjfighgbhhjedegfi","gigc","djhfcgfcfibjjdj","agajebcjjiifafgif","cbeficidfhaghbih","icbc","jjbgichdigidhbjecg","adcdceieb","hjeeeffedgijhjg","geabeeigjgaj","jiegfcigchdfccighag","bfgahbeeijfje","geaege","gdiae","bihbhhbbfbhjjiii","bhf","djdbhfgdeehh","cij","eehfgf","cgcaebff","ijc","fbidd","afgfchgig","dbdcgacagiadhchccc","fiahdchdfjfgdejfabjd","acaehdeg","agifibbdcfa","jbficcjhhjfdfigfif","cfiijahgihidbaebfda","icggfdjdadff","bggiefacbcgjcf","giddfidaagfdejbbajc","hgj","cic","ifhifcijdh","ggdgjidfhbj","acegbdeiedcice","jhedgigjhdgchhdbcbi","hhaebdgcgeacfbj","djdcad","cgecibdiehicbicdcb","bga","ahje","chddgdjjbci","bgbagjhgbihedeegjefj","higfja","jhddd","jcgcghfgjihidihe","cbedhaeccgbgj","jdbgjgfdjggiiddhgfgf","hadafbgiheciaehb","cgjhdeahcjacg","gifae","ghbbehjgeijajhaba","beahiigdejjggdf","agfcjebicjjjfedhi","ibagaefiifbfib","jfdehcggabcjiacdb","dcfggfijcchfhibdje","ahahgfgbcc","egaihebjfieddadihafe","fefhjciggfjjbeg","gaacababdgjfjjb","hjfhjfigg","jijfaccicajfghe","fdfejfghcbficacg","ibdheehahabgbceifbde","cjdaahaeg","cegigge","ifhcccaihgeae","jff","cdbgcaggcgih","ccgacjbieccdbbe","hgc","hhg","ihiceaeegfjjhdbffh","eb","gahdbhjieah","adhfbgfadcfe","cbciceg","hdafi","hhgidfjbhijjef","hcaeccccihbeihh","eeffiha","jhjfbagidehdcfahchjd","hjg","gfihjceifgagcdjciea","fiihfjcbf","eejdbhbeciigg","feb","dj","bdcbejfdddbgaii","hffejabcjeegejhhbijh","dhciee","gigaahaaadhedbija","bhbjabfjgcahjfhii","echjfajgi","ececjebhdjgc","gfdbifjh","iaeccjc","gbcdjfd","dfjibichdh","hijhcjegiabiefcfec","aahaghjifhgjhfjci","djadfahbhhaicjcfdib","jdahiigi","bcgcf","bgeecedhggegff","bbi","gcfbfbgjcccbhihhj","ddgjdddehdihfi","hgjhhaafdedf","ibabiid","dbfdfhchdfhbddcaegd","dfgigbgiajjdgec","eejhfbfiahaeiaf","dabjhegjiedffdhd","hicbcf","aadbcjffdggijeg","cggiidiggaahdbjfia","gicjghjbcigjiie","ghbaajfifgi","jda","beeeaghbdjfji","giheh","baagjfejgffhcjjf","chdbd","hd","deaecgcjabc","ehceaeebgbajf","jedhaeedfg","jcdhchafidedid","dbbcgeadeff","ighidh","cddfiicciccg","iehabgighefig","idfjcfbiiajg","eaececg","ajjfcciadhdfgdih","gbea","cfhghgjjjchaia","aaighhfeg","hjebdfa","eaafeajchheefhdc","cjfeegb","didihbiadfiebbe","bibcihjd","ejjfecjghh","hidffhcfedaagfj","ccbgbdhcgeebcj","edjjfeideheeficff","dii","jiighdbbgadhha","hdhfdei","ecc","bgibibjccjbbhecbg","cdbidffibibbighb","ig","iahhfa","dagdfgeiaf","hfeicfeffjjfd","fajacajaibdfhebc","habdfbeaejeabeahac","ebbafffdidfhef","igcefhjcfcfgcgice","fbhgaagaibiiejhdegaf","cih","fdehg","djgbf","ggijjfhjhhibi","eadbefidiah","ebiafhhggfgci","chfegfia","dd","didcijeabadjdc","geebifgegcjcgjdbhfbc","hfij","afhjij","cfedff","ia","iaa","ibaghj","efji","cieghgigbadbcgih","dbjjife","jjai","hgfidhg","icjdaf","jjaeeegce","dcg","bgahehacbfiacd","ejddddjcgchjgacbjj","bfggjgefdfechhcg","jbgjgbjffcifhbh","eedgehiecgcadiaf","jdacieaifdgfdbdb","jgbiaf","dfd","dh","fbibccg","ddfbaadfghceedbeeaj","iih","djbdbhchjj","aicfbbddbjdh","cafdga","jjbbhjjcff","eciededb","bdfbdafjfc","caacbf","ghhaiafcfcbbafeebj","hhcaibcjcgcdahgajcjh","bbajaabbjbjaib","figh","be","bjd","gbcicjfc","fhjbajbfd","acfbidgag","efgeabhehgaiifjcgii","jcgffajfa","ddbedcffccjheaacbgab","acjeiedicjdfcdgjaa","dgj","djjdbjffabjbd","jggdiheejacdfhgfje","acd","hdbhhfjgbibabcjffah","jddfgajibdbcbhi","djfagbecbfgjdbaaic","aajbhajijefabfehgijj","cehgcafdcicecghejbe","ehebbbeaegeg","ebbhegijeiajdc","hjajc","fddbedcieea","fibfhjei","habgehgcdghfeab","befhfbe","fjaacjei","ejhjfdjadffahdgbja","gcaihbeeeeeja","agedh","dfhgdjhhbfadg","gjfcfdb","geiidcdaaj","chdedibaafjbd","cecfcidaedfc","fddedidajbhgjdgcii","jahhihhfe","bajchgffbg","fajche","giajgdfjahdbdcafaacj","ddebaddec","didedbidg","hcbhabjafbadjfgcgi","iabicgcebaaicjj","bacief","dc","eifgad","hb","jfhjiebagdigdehiiif","ei","bfdijjbb","gaigghiefaacjgajdd","cbhi","iegfibffji","efaeci","agfjifghbgdijfjd","ib","dcha","ibjc","igjbeg","cadjigjcciggi","hdcddhbaaid","eccgfdecbhbbba","dicgbifjabeigdebebd","jghjcjaeiiibgci","ababbic","aigjfceajfhbddh","fijfbfeh","ehifde","ejgbi","abijaageehiajcjfa","ij","cf","ffigdbjfgi","facghejbjagccjhbdggj","fcdifd","gdeajhfebdiddcjfhae","giiihhiefdaejd","cbiacbcihggejagdeej","jdcehdbcbgff","ccdjbeb","ieibigieahbgggeh","hc","hcjbigbbfiagg","heaihabgh","bgdcccaaacdadjdeddg","jfagie","fhgdjfiacahcbhj","baidccdhacb","bfeebjhfjahhfhhhcb","ceddifeea","dfdbfdebfbddifddjd","adhefhcibhigdcb","ecgcfeiebdjhfdcg","dibadacb","higeeje","dijgbighccjf","jjfjhabbii","ihcihecjedgihe","hcdfd","fgdafecdegjfe","hfadcjfjjgfh","gfhdcbacd","fgbibeeacigecdfdifca","gfg","digicijbgghiihdf","efghfihhbbdcehb","fdjfbabefcfhhgcgjdi","ajbggefdccbd","dfihegfjjjc","acbbbjff","bbhehibgegbbde","cibhaddfdfca","hjeghicdadbgagafce","hebiagfec","aibibe","diadjabcdccbg","ag","hbgdheeg","cdchfajjbc","egecci","hjhhjbeecaeceechi","jbg","gaagaaejh","ijbej","ghdgaaf","ddfggeeefhcfcgicdceb","iaeaajiedabeeafbcjfb","dfghdifjghjjahcgidd","hddcfaadga","eaecfjhcaa","hgggfejbhchffgja","ej","jcbheedfgabfc","fcahhcga","ehecjfhdbgae","gifbcgjfgjda","cbfhdfc","fgeeghabdagdbjcb","gfhcdcdiggghi","eg","ba","ihaj","chdfijiahfieiefidh","fdjghieeffgbcaggejb","echdjbicghfehejide","jbdiaiabgahijgg","ebeffcfcbfce","ddififjjbdebgiighjhe","gedajefibbgfadbddi","fjidegcg","cecgd","ebhcgdjfih","bgjg","bfaj","icjeiaejehhjbigb","eeefaaf","beijffhebcecjbb","hbedg","icjgfidfc","ciebgbgjdiceda","jbajcjc","iceeeaehi","ecb","aaagdfggdhecijf","fehjdcfij","hajgdfgaejgjhacabii","hcjbbaij","ghcg","fhcgegdedbeieabajfa","fjafdbdaibijhi","fbbdh","aicjgdggbddbeaig","bdjaefjifgfgddb","jjcadhdbfghgbefifdgc","hhiaabdjcbdgdegab","dbjahgbgaigecdbhd","fhead","giaccb","caihachgbh","iafjbhjhaf","cfbg","fhehadbgcgaahaccei","aagjbiehd","bbbfccjcbecgdfaj","igidhaeeibabiibfgd","ghadiffhiabaagi","fjgheha","hegfdcebebfbahj","cfjgeaeihibdcbid","ddhabaj","cdibggbi","bccf","fhiffaaeihdjddjdhcc","jdifgbceecibcgfgbaj","bdccgdjghd","eajhahaejh","ajjdjdhbjdbheedgfaf","hieeiaf","cihf","hdbiffej","deb","jehjdhjcbdihgaabcg","eehcdfbhececiaih","jh","ecea","fbeceehejfid","ebbdbaecbjbbbjijdif","ihgdgfdibcgbfde","fcfbfefadgehhdhfgh","edhafgeabdc","gaaeegjjdacicejegh","hi","ieaic","gbc","iibjcbeg","cc","ebhdhgfe","iebggabcjhhihifeae","ghedjjajcdg","dbfggcjbbhibjddijfia","gid","bibjcej","cjfbjcecfiahjhgjgjga","cfeabcdi"]
words = ["abcd","dcba","lls","s","sssll"]
start = time.time()
print(Solution.palindromePairs(None,words))
print('过去了%s秒'%(time.time()-start))




