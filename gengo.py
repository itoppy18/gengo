#!/usr/bin/python3
#©2018 Mamoru Itoi

import random

kanjiList = ['人', '女', '田', '木', '糸', '土', '一', '口', '水', '音', '右', '雨', '日', '火', '金', '円', '手', '犬', '王', '玉', '大', '山', '下', '力', '花', '貝', '竹', '虫', '白', '夕', '見', '車', '石', '学', '子', '目', '気', '月', '九', '休', '足', '八', '十', '立', '空', '五', '二', '校', '左', '三', '生', '四', '字', '耳', '七', '赤', '出', '小', '上', '森', '正', '青', '千', '川', '先', '入', '早', '草', '村', '男', '中', '町', '天', '年', '文', '百', '本', '名', '林', '六', '肉', '心', '引', '弓', '食', '羽', '雲', '言', '行', '馬', '走', '門', '園', '遠', '色', '何', '科', '夏', '家', '歌', '画', '回', '会', '海', '絵', '角', '外', '楽', '活', '刀', '間', '丸', '岩', '顔', '汽', '記', '帰', '止', '方', '牛', '工', '魚', '京', '強', '教', '矢', '近', '兄', '形', '計', '鳥', '元', '原', '戸', '古', '午', '後', '語', '公', '広', '交', '光', '考', '高', '黄', '合', '谷', '国', '黒', '今', '才', '細', '作', '算', '市', '姉', '思', '紙', '寺', '自', '時', '室', '社', '弱', '首', '秋', '週', '里', '春', '書', '少', '米', '場', '新', '親', '図', '数', '西', '声', '星', '晴', '切', '雪', '船', '線', '前', '組', '多', '太', '体', '台', '地', '池', '知', '茶', '昼', '長', '朝', '直', '通', '弟', '店', '点', '電', '冬', '当', '東', '答', '頭', '同', '道', '読', '内', '南', '売', '買', '麦', '半', '番', '父', '風', '分', '聞', '歩', '母', '北', '毎', '妹', '万', '明', '鳴', '毛', '夜', '野', '友', '用', '曜', '来', '理', '話', '悪', '安', '暗', '医', '委', '意', '育', '員', '院', '飲', '運', '泳', '皿', '駅', '央', '横', '屋', '温', '化', '荷', '界', '開', '階', '寒', '感', '漢', '館', '岸', '起', '期', '羊', '客', '究', '急', '級', '宮', '球', '去', '橋', '業', '曲', '局', '銀', '区', '苦', '具', '君', '係', '軽', '血', '決', '研', '県', '庫', '湖', '向', '幸', '港', '号', '根', '祭', '仕', '死', '使', '始', '指', '歯', '詩', '次', '事', '持', '式', '実', '写', '者', '主', '守', '取', '酒', '受', '州', '拾', '終', '習', '集', '住', '重', '宿', '所', '暑', '助', '昭', '消', '商', '章', '勝', '乗', '植', '申', '身', '神', '真', '深', '進', '世', '整', '昔', '全', '相', '送', '想', '息', '速', '族', '他', '打', '対', '待', '代', '第', '題', '炭', '短', '談', '着', '注', '柱', '丁', '帳', '調', '追', '定', '庭', '笛', '鉄', '転', '都', '度', '投', '豆', '島', '湯', '登', '等', '動', '童', '農', '波', '配', '倍', '箱', '畑', '発', '反', '坂', '板', '皮', '悲', '美', '鼻', '筆', '氷', '表', '秒', '病', '品', '負', '部', '服', '福', '物', '平', '返', '勉', '放', '味', '命', '面', '問', '役', '薬', '由', '油', '有', '遊', '予', '洋', '葉', '陽', '様', '落', '流', '旅', '両', '緑', '礼', '列', '練', '路', '和', '愛', '案', '以', '衣', '位', '囲', '胃', '士', '印', '英', '栄', '塩', '欠', '億', '加', '果', '貨', '課', '芽', '改', '械', '害', '街', '各', '覚', '完', '官', '管', '関', '観', '願', '希', '季', '紀', '喜', '旗', '器', '機', '議', '求', '泣', '救', '給', '挙', '漁', '共', '協', '鏡', '競', '極', '訓', '軍', '郡', '径', '型', '景', '芸', '結', '建', '健', '験', '固', '功', '好', '老', '候', '航', '康', '告', '差', '菜', '最', '材', '昨', '札', '刷', '殺', '察', '参', '産', '散', '残', '氏', '史', '司', '試', '児', '治', '辞', '失', '借', '種', '周', '祝', '順', '初', '松', '笑', '唱', '焼', '象', '照', '賞', '臣', '信', '成', '省', '清', '静', '席', '積', '折', '節', '説', '浅', '戦', '選', '然', '争', '倉', '巣', '束', '側', '続', '卒', '孫', '帯', '隊', '達', '単', '置', '仲', '貯', '兆', '腸', '低', '底', '停', '的', '典', '伝', '徒', '努', '灯', '堂', '働', '特', '得', '毒', '熱', '念', '敗', '梅', '博', '飯', '飛', '費', '必', '票', '標', '不', '夫', '付', '府', '副', '粉', '兵', '別', '辺', '変', '便', '包', '法', '望', '牧', '末', '満', '未', '脈', '民', '無', '約', '勇', '要', '養', '浴', '利', '陸', '良', '料', '量', '輪', '類', '令', '冷', '例', '歴', '連', '労', '録', '圧', '移', '因', '永', '営', '衛', '易', '益', '液', '演', '応', '往', '桜', '恩', '可', '仮', '価', '河', '過', '示', '賀', '快', '解', '格', '確', '額', '刊', '幹', '慣', '眼', '基', '寄', '規', '技', '義', '逆', '久', '旧', '居', '許', '境', '均', '禁', '句', '群', '経', '潔', '件', '券', '険', '検', '限', '現', '減', '故', '個', '護', '効', '厚', '耕', '鉱', '構', '興', '講', '混', '査', '再', '災', '妻', '採', '際', '在', '財', '罪', '雑', '酸', '賛', '支', '志', '枝', '師', '資', '飼', '似', '識', '質', '舎', '舌', '謝', '授', '修', '述', '術', '準', '序', '招', '承', '証', '条', '状', '常', '情', '織', '職', '制', '性', '政', '勢', '精', '製', '税', '責', '績', '接', '設', '絶', '銭', '祖', '素', '総', '造', '像', '増', '則', '測', '属', '率', '損', '退', '貸', '態', '団', '断', '築', '張', '提', '程', '適', '敵', '統', '銅', '導', '徳', '独', '任', '燃', '能', '破', '犯', '判', '版', '比', '肥', '非', '備', '俵', '評', '貧', '布', '婦', '富', '武', '復', '複', '仏', '編', '弁', '保', '墓', '報', '豊', '防', '貿', '暴', '務', '夢', '迷', '綿', '輸', '余', '預', '容', '略', '留', '領', '寸', '異', '遺', '域', '宇', '映', '延', '沿', '革', '我', '灰', '骨', '拡', '閣', '割', '株', '干', '巻', '看', '簡', '危', '机', '揮', '貴', '疑', '吸', '穴', '供', '胸', '郷', '勤', '筋', '系', '敬', '警', '劇', '激', '絹', '権', '憲', '源', '厳', '己', '呼', '誤', '后', '孝', '皇', '紅', '降', '鋼', '刻', '穀', '困', '砂', '座', '済', '裁', '策', '冊', '蚕', '至', '私', '姿', '視', '詞', '誌', '磁', '射', '捨', '尺', '若', '樹', '収', '宗', '就', '衆', '従', '縦', '縮', '熟', '純', '処', '署', '諸', '除', '将', '傷', '障', '城', '蒸', '針', '仁', '垂', '推', '盛', '聖', '誠', '宣', '専', '泉', '洗', '染', '善', '奏', '窓', '創', '装', '層', '操', '蔵', '臓', '存', '尊', '宅', '担', '探', '誕', '段', '暖', '値', '宙', '忠', '著', '庁', '頂', '潮', '賃', '痛', '展', '討', '党', '糖', '届', '難', '乳', '認', '納', '脳', '派', '拝', '背', '肺', '俳', '片', '班', '晩', '否', '批', '秘', '腹', '奮', '並', '陛', '閉', '補', '暮', '宝', '訪', '亡', '忘', '棒', '枚', '幕', '密', '盟', '模', '訳', '郵', '優', '幼', '欲', '翌', '乱', '卵', '覧', '裏', '律', '臨', '朗', '論', '亜', '哀', '握', '扱', '依', '威', '為', '尉', '偉', '違', '維', '慰', '緯', '壱', '逸', '芋', '姻', '陰', '隠', '韻', '詠', '影', '鋭', '疫', '悦', '越', '謁', '閲', '炎', '宴', '援', '煙', '猿', '鉛', '縁', '汚', '凹', '押', '欧', '殴', '翁', '奥', '憶', '虞', '乙', '卸', '穏', '佳', '架', '華', '菓', '渦', '嫁', '暇', '禍', '靴', '寡', '箇', '稼', '蚊', '雅', '餓', '介', '戒', '怪', '拐', '悔', '皆', '塊', '壊', '懐', '劾', '涯', '慨', '該', '概', '垣', '核', '殻', '郭', '較', '隔', '獲', '嚇', '穫', '岳', '掛', '潟', '括', '喝', '渇', '滑', '褐', '轄', '且', '刈', '甘', '汗', '缶', '肝', '冠', '陥', '乾', '勘', '患', '貫', '喚', '堪', '換', '敢', '棺', '款', '閑', '勧', '寛', '歓', '監', '緩', '憾', '還', '環', '艦', '鑑', '含', '頑', '企', '岐', '忌', '奇', '祈', '軌', '既', '飢', '鬼', '幾', '棋', '棄', '輝', '騎', '宜', '偽', '欺', '儀', '戯', '擬', '犠', '菊', '吉', '喫', '詰', '却', '脚', '虐', '及', '丘', '朽', '糾', '窮', '巨', '拒', '拠', '虚', '距', '御', '凶', '叫', '狂', '享', '況', '峡', '挟', '狭', '恐', '恭', '脅', '矯', '響', '驚', '仰', '暁', '凝', '斤', '菌', '琴', '緊', '謹', '襟', '吟', '駆', '愚', '偶', '遇', '隅', '屈', '掘', '繰', '勲', '薫', '刑', '茎', '契', '恵', '啓', '掲', '渓', '蛍', '傾', '携', '継', '慶', '憩', '鶏', '迎', '鯨', '撃', '傑', '肩', '倹', '兼', '剣', '軒', '圏', '堅', '嫌', '献', '遣', '賢', '謙', '繭', '顕', '懸', '幻', '玄', '弦', '孤', '弧', '枯', '雇', '誇', '鼓', '顧', '互', '呉', '娯', '悟', '碁', '孔', '巧', '甲', '江', '坑', '抗', '攻', '更', '拘', '肯', '侯', '恒', '洪', '荒', '郊', '香', '貢', '控', '慌', '硬', '絞', '項', '溝', '綱', '酵', '稿', '衡', '購', '拷', '剛', '豪', '克', '酷', '獄', '込', '昆', '恨', '婚', '紺', '魂', '墾', '懇', '佐', '唆', '詐', '鎖', '砕', '宰', '栽', '彩', '斎', '債', '催', '歳', '載', '剤', '崎', '削', '索', '酢', '搾', '錯', '咲', '撮', '擦', '桟', '惨', '傘', '暫', '旨', '伺', '刺', '祉', '肢', '畝', '舟', '施', '脂', '紫', '嗣', '雌', '賜', '諮', '侍', '滋', '慈', '辛', '璽', '軸', '疾', '執', '湿', '漆', '芝', '赦', '斜', '煮', '遮', '邪', '蛇', '酌', '釈', '爵', '寂', '朱', '狩', '殊', '珠', '趣', '寿', '需', '儒', '囚', '秀', '臭', '愁', '酬', '醜', '襲', '汁', '充', '柔', '渋', '銃', '獣', '叔', '淑', '粛', '塾', '俊', '瞬', '旬', '巡', '盾', '准', '殉', '循', '潤', '遵', '庶', '緒', '如', '叙', '徐', '升', '召', '匠', '床', '抄', '肖', '尚', '昇', '沼', '宵', '症', '祥', '渉', '紹', '訟', '掌', '晶', '焦', '硝', '粧', '詔', '奨', '詳', '彰', '衝', '償', '礁', '鐘', '丈', '冗', '浄', '剰', '畳', '縄', '壌', '嬢', '錠', '譲', '醸', '殖', '飾', '触', '嘱', '辱', '伸', '侵', '津', '唇', '娠', '振', '浸', '紳', '診', '寝', '慎', '審', '震', '薪', '刃', '尽', '迅', '甚', '陣', '尋', '吹', '炊', '帥', '粋', '衰', '酔', '遂', '睡', '穂', '随', '髄', '枢', '崇', '据', '杉', '瀬', '是', '井', '姓', '征', '斉', '牲', '逝', '斗', '婿', '誓', '請', '斥', '析', '隻', '惜', '跡', '籍', '拙', '窃', '摂', '仙', '占', '扇', '栓', '旋', '践', '潜', '遷', '薦', '繊', '鮮', '禅', '漸', '繕', '阻', '租', '措', '粗', '疎', '訴', '塑', '礎', '双', '壮', '荘', '捜', '挿', '桑', '掃', '曹', '喪', '葬', '僧', '遭', '槽', '燥', '霜', '騒', '藻', '憎', '贈', '即', '促', '俗', '賊', '妥', '堕', '惰', '駄', '耐', '怠', '胎', '泰', '袋', '逮', '替', '滞', '滝', '択', '沢', '卓', '拓', '託', '濯', '諾', '濁', '但', '脱', '奪', '棚', '丹', '胆', '淡', '嘆', '端', '鍛', '弾', '壇', '恥', '致', '遅', '痴', '稚', '畜', '逐', '蓄', '秩', '窒', '嫡', '沖', '抽', '衷', '鋳', '駐', '弔', '挑', '彫', '眺', '釣', '超', '跳', '徴', '澄', '聴', '懲', '勅', '沈', '珍', '朕', '陳', '鎮', '墜', '塚', '漬', '坪', '呈', '廷', '抵', '邸', '亭', '貞', '帝', '訂', '逓', '偵', '堤', '艇', '締', '泥', '摘', '滴', '迭', '哲', '徹', '撤', '添', '殿', '吐', '途', '渡', '塗', '奴', '怒', '到', '逃', '浦', '倒', '凍', '唐', '桃', '透', '悼', '盗', '陶', '塔', '搭', '棟', '痘', '筒', '稲', '踏', '謄', '闘', '騰', '洞', '胴', '峠', '匿', '督', '篤', '凸', '突', '屯', '豚', '鈍', '曇', '軟', '尼', '弐', '尿', '妊', '忍', '寧', '粘', '悩', '濃', '把', '覇', '婆', '杯', '排', '廃', '輩', '培', '陪', '媒', '賠', '伯', '拍', '泊', '迫', '舶', '薄', '漠', '縛', '爆', '肌', '鉢', '髪', '伐', '抜', '罰', '閥', '帆', '伴', '畔', '般', '販', '搬', '煩', '頒', '範', '繁', '藩', '蛮', '盤', '妃', '彼', '披', '卑', '疲', '被', '扉', '碑', '罷', '避', '尾', '微', '匹', '泌', '姫', '漂', '苗', '描', '猫', '浜', '賓', '頻', '敏', '瓶', '扶', '怖', '附', '赴', '浮', '符', '普', '腐', '敷', '膚', '賦', '譜', '侮', '舞', '封', '伏', '幅', '覆', '払', '沸', '紛', '雰', '噴', '墳', '憤', '丙', '併', '柄', '塀', '幣', '弊', '壁', '癖', '偏', '遍', '捕', '舗', '募', '慕', '簿', '芳', '邦', '奉', '抱', '泡', '胞', '俸', '倣', '峰', '砲', '崩', '飽', '褒', '縫', '乏', '又', '忙', '坊', '妨', '房', '肪', '某', '冒', '剖', '紡', '傍', '帽', '膨', '謀', '朴', '僕', '墨', '撲', '没', '堀', '奔', '翻', '凡', '盆', '麻', '摩', '磨', '魔', '埋', '膜', '抹', '慢', '漫', '魅', '岬', '妙', '眠', '矛', '霧', '娘', '銘', '滅', '免', '茂', '妄', '盲', '耗', '猛', '網', '黙', '紋', '厄', '躍', '愉', '諭', '癒', '唯', '幽', '悠', '猶', '裕', '雄', '誘', '憂', '融', '与', '誉', '庸', '揚', '揺', '溶', '腰', '踊', '窯', '擁', '謡', '抑', '翼', '裸', '羅', '雷', '頼', '絡', '酪', '濫', '欄', '吏', '痢', '履', '離', '柳', '竜', '粒', '隆', '硫', '虜', '慮', '了', '涼', '猟', '陵', '僚', '寮', '療', '糧', '厘', '倫', '隣', '涙', '累', '塁', '励', '戻', '鈴', '零', '霊', '隷', '齢', '麗', '暦', '劣', '烈', '裂', '恋', '廉', '錬', '炉', '露', '郎', '浪', '廊', '楼', '漏', '賄', '惑', '枠', '湾', '腕', '挨', '曖', '宛', '嵐', '爪', '畏', '萎', '椅', '彙', '茨', '咽', '阜', '淫', '唄', '鬱', '怨', '媛', '艶', '旺', '岡', '臆', '俺', '苛', '牙', '瓦', '楷', '潰', '諧', '崖', '蓋', '骸', '柿', '顎', '葛', '釜', '鎌', '韓', '玩', '伎', '巾', '亀', '毀', '畿', '臼', '嗅', '僅', '錦', '惧', '串', '窟', '熊', '詣', '憬', '稽', '隙', '桁', '拳', '鍵', '舷', '股', '虎', '錮', '勾', '梗', '喉', '乞', '傲', '駒', '頃', '痕', '沙', '挫', '采', '塞', '埼', '柵', '刹', '拶', '斬', '恣', '摯', '餌', '鹿', '叱', '嫉', '腫', '呪', '袖', '羞', '蹴', '憧', '拭', '尻', '芯', '腎', '須', '裾', '凄', '醒', '脊', '戚', '煎', '羨', '腺', '詮', '箋', '膳', '狙', '遡', '曽', '爽', '痩']

def main():
	for i in range(4822416):
		f = random.choice(kanjiList)
		s = random.choice(kanjiList)
		gengoList.append(f + s)
	print(gengoList)
main()
