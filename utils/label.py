"""
Copyright 2020- Kai.Lib
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
      http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from utils.define import logger

def get_label(filepath, sos_id=2037, eos_id=2038, target_dict=None):
    """
    Provides specific file`s label to list format.
    Inputs: filepath, bos_id, eos_id, target_dict
        - **filepath**: specific path of label file
        - **bos_id**: <s>`s id
        - **eos_id**: </s>`s id
        - **target_dict**: dictionary of filename and labels
                Format : {KaiSpeech_label_FileNum : '5 0 49 4 0 8 190 0 78 115', ... }
    Outputs: label
        - **label**: list of bos + sequence of label + eos
                Format : [<s>, 5, 0, 49, 4, 0, 8, 190, 0, 78, 115, </s>]
    """
    if target_dict == None: logger.info("target_dict is None")
    key = filepath.split('/')[-1].split('.')[0]
    script = target_dict[key]
    tokens = script.split(' ')

    label = list()
    label.append(int(sos_id))
    for token in tokens:
        label.append(int(token))
    label.append(int(eos_id))
    del script, tokens # memory deallocation

    return label

def label_to_string(labels, index2char, EOS_token):
    if len(labels.shape) == 1:
        sent = str()
        for i in labels:
            if i.item() == EOS_token:
                break
            sent += index2char[i.item()]
        return sent

    elif len(labels.shape) == 2:
        sents = list()
        for i in labels:
            sent = str()
            for j in i:
                if j.item() == EOS_token:
                    break
                sent += index2char[j.item()]
            sents.append(sent)
        return sents