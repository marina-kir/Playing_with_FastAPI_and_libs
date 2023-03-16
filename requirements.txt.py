import os
# import sys
# from fuzzywuzzy import fuzz
import subprocess

path = "C:/Users/mkirnaso/Downloads/careai.gait.docker-master-1/careai.gait.docker-master"
path = "C:/Users/mkirnaso/Downloads/careai.ROM.algo-e4b1d5210e68cf751b9923339f198ad7411b8dae/careai.ROM.algo-e4b1d5210e68cf751b9923339f198ad7411b8dae"
path = "C:/Users/mkirnaso/Downloads/careai.gait.algo-180ccb052dfd684e11b16c87e1fb016439bfbf6a/careai.gait.algo-180ccb052dfd684e11b16c87e1fb016439bfbf6a"
path = "C:/Users/mkirnaso/Downloads/HRNet_human_body/HRNet_human_body_pose_inference"

path = "C:/Users/mkirnaso/Downloads/careai.algo.android-master/careai.algo.android-master"
path = "C:/Users/mkirnaso/Downloads/careai.algo.core-9294da6a0ad9e877925a9b02e3f43342618fdcbb/careai.algo.core-9294da6a0ad9e877925a9b02e3f43342618fdcbb"

path = "C:/Users/mkirnaso/Downloads/os.linux.yocto.edgeai-platform-master/os.linux.yocto.edgeai-platform-master"

#########################

path = "C:/Users/mkirnaso/Downloads/careai.algo.android-master-2/careai.algo.android-master"
path = "C:/Users/mkirnaso/Downloads/careai.algo.core-2/careai.algo.core-9294da6a0ad9e877925a9b02e3f43342618fdcbb"
path = "C:/Users/mkirnaso/Downloads/careai.gait.algo-2/careai.gait.algo-180ccb052dfd684e11b16c87e1fb016439bfbf6a"
path = "C:/Users/mkirnaso/Downloads/careai.gait.docker-master-2/careai.gait.docker-master"
path = "C:/Users/mkirnaso/Downloads/careai.ROM.algo-2/careai.ROM.algo-e4b1d5210e68cf751b9923339f198ad7411b8dae"
path = "C:/Users/mkirnaso/Downloads/HRNet_human_body_pose_inference-2/HRNet_human_body_pose_inference-47de45afd004d526e7181fba9d3ea29399663051"
path = "C:/Users/mkirnaso/Downloads/os.linux.yocto.edgeai-platform-master-2/os.linux.yocto.edgeai-platform-master"

###########

path = "C:/Users/mkirnaso/Downloads/os.linux.yocto.edgeai-manifests2/os.linux.yocto.edgeai-manifests-hardknott"



'''
Cloud:
https://github.com/intel-sandbox/careai.gait.docker
              submodules:
              https://github.com/intel-sandbox/careai.ROM.algo/tree/e4b1d5210e68cf751b9923339f198ad7411b8dae
              https://github.com/intel-sandbox/careai.gait.algo/tree/180ccb052dfd684e11b16c87e1fb016439bfbf6a
              https://github.com/intel-sandbox/HRNet_human_body_pose_inference/tree/47de45afd004d526e7181fba9d3ea29399663051
Tablet:
https://github.com/intel-sandbox/careai.algo.android
              Submodules:
              https://github.com/intel-sandbox/careai.algo.core/tree/9294da6a0ad9e877925a9b02e3f43342618fdcbb
Device:
https://github.com/intel-innersource/os.linux.yocto.edgeai-platform  (handled by the Finish team)


'''




files = os.listdir(path)
pyfiles = []
for root, dirs, files in os.walk(path):
      for file in files:
        if file.endswith('.py'):
              pyfiles.append(os.path.join(root, file))

stopWords = ['from', 'import',',','.']

importables = []

for file in pyfiles:
    with open(file) as f:
        content = f.readlines()

        for line in content:
            if "import" in line:
                for sw in stopWords:
                    line = ' '.join(line.split(sw))

                importables.append(line.strip().split(' ')[0])

importables = sorted(list(dict.fromkeys(importables)))
with open(f"{path}/requirements.txt", 'w') as fp:
    for item in importables:
        fp.write("%s\n" % item)


# importables = set(importables)
# subprocess.call(f"pip freeze > {path}/requirements.txt", shell=True)