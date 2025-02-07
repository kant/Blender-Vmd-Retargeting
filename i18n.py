import bpy

dict = {
    "en_US":{
        (None, "Select Vmd File"):"Select Vmd File",
        (None, "Select Avatar Type"):"Select Avatar Type",
        (None, "Select Model Type:"):"Select Model Type:",
        (None, "High Heel"):"High Heel",
        (None, "Check to ignore foot rotation"):"Check to ignore foot rotation",
        (None, "Body"):"Body",
        (None, "Check to import body motion"):"Check to import body motion",
        (None, "Must uncheck Rename bones when importing mmd model"):"Must uncheck Rename bones when importing mmd model",
        (None, "Upperarm"):"Upperarm",
        (None, "Forearm"):"Forearm",
        (None, "Only works when retargeting from vmd file"):"Only works when retargeting from vmd file",
        (None, "Eyeball"):"Eyeball",
        (None, "Check to import eyeball motion"):"Check to import eyeball motion",
        (None, "Facial"):"Facial",
        (None, "Check to import facial motion"):"Check to import facial motion",
        (None, "Viseme"):"Viseme",
        (None, "Check to import Viseme motion"):"Check to import Viseme motion",
        (None, "Interpolation type, does not affect on camera"):"Interpolation type, does not affect on camera",
        (None, "Easing type, does not affect on camera"):"Easing type, does not affect on camera",
        (None, "Check to import camera motion"):"Check to import camera motion",
        (None, "Rate"):"Rate",
        (None, "Camera Rate"):"Camera Rate",
        (None, "Height Offset(cm)"):"Height Offset(cm)",
        (None, "Move Up 8cm if model is on high heel"):"Move Up 8cm if model is on high heel",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"It gonna slow down the retargeting a lot, only check it when importing a pose",
        (None, "Nothing selected"):"Nothing selected",
        (None, "Pls select an Armature, mesh or camera"):"Pls select an Armature, mesh or camera",
        (None, "Check to import:"):"Check to import:",
        (None, "Arm rotation rate:"):"Arm rotation rate:",
        (None, "Or pick a MMD model as source:"):"Or pick a MMD model as source:",
        (None, "Easing:"):"Easing:",
        (None, "Camera Setting:"):"Camera Setting:",
        (None, "Debug Mode"):"Debug Mode",
        (None, "Execute"):"Execute",
        
    },
    "zh_CN":{
        (None, "Select Vmd File"):"选择vmd文件",
        (None, "Select Avatar Type"):"选择模型类型",
        (None, "Select Model Type:"):"选择模型类型:",
        (None, "High Heel"):"高跟鞋",
        (None, "Check to ignore foot rotation"):"勾选后无视脚踝旋转",
        (None, "Body"):"身体",
        (None, "Check to import body motion"):"勾选导入身体运动",
        (None, "Must uncheck Rename bones when importing mmd model"):"导入mmd模型时，必须取消勾选重命名骨骼",
        (None, "Upperarm"):"上臂",
        (None, "Forearm"):"前臂",
        (None, "Only works when retargeting from vmd file"):"只在从vmd文件导入时有效",
        (None, "Eyeball"):"眼球",
        (None, "Check to import eyeball motion"):"勾选导入眼球运动",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"勾选导入表情",
        (None, "Viseme"):"口型",
        (None, "Check to import Viseme motion"):"勾选导入口型",
        (None, "Interpolation type, does not affect on camera"):"补间曲线类型，不影响摄像机",
        (None, "Easing type, does not affect on camera"):"平滑过渡类型，不影响摄像机",
        (None, "Check to import camera motion"):"勾选导入摄像机运动",
        (None, "Rate"):"调整比例",
        (None, "Camera Rate"):"调整比例",
        (None, "Height Offset(cm)"):"高度偏移(cm)",
        (None, "Move Up 8cm if model is on high heel"):"模型有高跟鞋可上调8厘米",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"会明显拖慢转换过程，只在导入单个动作时启用",
        (None, "Nothing selected"):"没有选择导入任何东西",
        (None, "Pls select an Armature, mesh or camera"):"请选择一个骨骼，模型或摄像机",
        (None, "Check to import:"):"勾选导入:",
        (None, "Arm rotation rate:"):"手臂旋转比例:",
        (None, "Or pick a MMD model as source:"):"或选择一个mmd模型作为源:",
        (None, "Easing:"):"平滑过渡:",
        (None, "Camera Setting:"):"摄影机设置:",
        (None, "Debug Mode"):"调试模式",
        (None, "Execute"):"执行",
    },
    "zh_TW":{
        (None, "Select Vmd File"):"選擇vmd文件",
        (None, "Select Avatar Type"):"選擇模型類型",
        (None, "Select Model Type:"):"選擇模型類型:",
        (None, "High Heel"):"高跟鞋",
        (None, "Check to ignore foot rotation"):"勾選後無視腳踝旋轉",
        (None, "Body"):"身體",
        (None, "Check to import body motion"):"勾選導入身體運動",
        (None, "Must uncheck Rename bones when importing mmd model"):"導入mmd模型時，必須取消勾選重命名骨骼",
        (None, "Upperarm"):"上臂",
        (None, "Forearm"):"前臂",
        (None, "Only works when retargeting from vmd file"):"只在從vmd文件導入時有效",
        (None, "Eyeball"):"眼球",
        (None, "Check to import eyeball motion"):"勾選導入眼球運動",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"勾選導入表情",
        (None, "Viseme"):"口型",
        (None, "Check to import Viseme motion"):"勾選導入口型",
        (None, "Interpolation type, does not affect on camera"):"補間曲線類型，不影響攝像機",
        (None, "Easing type, does not affect on camera"):"平滑過渡類型，不影響攝像機",
        (None, "Check to import camera motion"):"勾選導入攝像機運動",
        (None, "Rate"):"調整比例",
        (None, "Camera Rate"):"調整比例",
        (None, "Height Offset(cm)"):"高度偏移(cm)",
        (None, "Move Up 8cm if model is on high heel"):"模型有高跟鞋可上調8厘米",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"會明顯拖慢轉換過程，只在導入單個動作時啟用",
        (None, "Nothing selected"):"沒有選擇導入任何東西",
        (None, "Pls select an Armature, mesh or camera"):"請選擇一個骨骼，模型或攝像機",
        (None, "Check to import:"):"勾選導入:",
        (None, "Arm rotation rate:"):"手臂旋轉比例:",
        (None, "Or pick a MMD model as source:"):"或選擇一個mmd模型作為源:",
        (None, "Easing:"):"平滑過渡:",
        (None, "Camera Setting:"):"攝影機設定:",
        (None, "Debug Mode"):"調試模式",
        (None, "Execute"):"執行",
    },
    "ja_JP":{
        (None, "Select Vmd File"):"Vmdファイルを選択",
        (None, "Select Avatar Type"):"アバターのタイプを選択",
        (None, "Select Model Type:"):"モデルのタイプを選択:",
        (None, "High Heel"):"ハイヒール",
        (None, "Check to ignore foot rotation"):"足首の回転を無視",
        (None, "Body"):"ボディ",
        (None, "Check to import body motion"):"ボディモーションをインポート",
        (None, "Must uncheck Rename bones when importing mmd model"):"mmdモデルを読み込むときは、[ボーンの名前を変更]をオフにする必要があります",
        (None, "Upperarm"):"腕",
        (None, "Forearm"):"ひじ",
        (None, "Only works when retargeting from vmd file"):"vmdファイルからのインポート時にのみ有効",
        (None, "Eyeball"):"目",
        (None, "Check to import eyeball motion"):"眼球モーションをインポート",
        (None, "Facial"):"表情",
        (None, "Check to import facial motion"):"表情モーションをインポート",
        (None, "Viseme"):"リップ",
        (None, "Check to import Viseme motion"):"リップモーションをインポート",
        (None, "Interpolation type, does not affect on camera"):"補間曲線を、カメラに影響なし",
        (None, "Easing type, does not affect on camera"):"スムーズタイプ、カメラに影響なし ",
        (None, "Check to import camera motion"):"カメラモーションをインポート",
        (None, "Rate"):"レート",
        (None, "Camera Rate"):"カメラレート",
        (None, "Height Offset(cm)"):"高さオフセット(cm)",
        (None, "Move Up 8cm if model is on high heel"):"ハイヒールをいるの場合は、8cm上に移動してください",
        (None, "It gonna slow down the retargeting a lot, only check it when importing a pose"):"読み込み速度が大幅に低下するため、1つのポーズを読み込む場合にのみ使用してください",
        (None, "Nothing selected"):"何も選択されていません",
        (None, "Pls select an Armature, mesh or camera"):"スケルトン、メッシュ、またはカメラを選択してください",
        (None, "Check to import:"):"チェックしてインポート:",
        (None, "Arm rotation rate:"):"腕の回転スケール:",
        (None, "Or pick a MMD model as source:"):"またはソースとしてmmdモデルを選択します:",
        (None, "Easing:"):"スムーズ:",
        (None, "Camera Setting:"):"カメラの設定:",
        (None, "Debug Mode"):"デバッグモード",
        (None, "Execute"):"実行",
    },
}


def register():
    bpy.app.translations.register(__name__, dict)

def unregister():
    bpy.app.translations.unregister(__name__)

# need register
def word(msg_id):
    return bpy.app.translations.pgettext(msg_id)

# do not need register, but need to reboot blender
def word2(msg_id):
    lang = bpy.app.translations.locale
    msg_key = (None, msg_id)

    word = msg_id
    if lang in dict.keys():
        if msg_key in dict[lang].keys():
            word = dict[lang][msg_key]

    return word


