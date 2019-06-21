# Copyright 2019 The Magenta Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A setuptools based setup module for magenta."""

import sys

from setuptools import find_packages
from setuptools import setup

# Bit of a hack to parse the version string stored in version.py without
# executing __init__.py, which will end up requiring a bunch of dependencies to
# execute (e.g., tensorflow, pretty_midi, etc.).
# Makes the __version__ variable available.
with open('magenta/version.py') as in_file:
  exec(in_file.read())  # pylint: disable=exec-used

if '--gpu' in sys.argv:
  gpu_mode = True
  sys.argv.remove('--gpu')
else:
  gpu_mode = False

REQUIRED_PACKAGES = [
    'IPython',
    'absl-py',
    'Pillow >= 3.4.2',
    'backports.tempfile',
    'bokeh >= 0.12.0',
    'intervaltree >= 2.1.0',
    'joblib >= 0.12',
    'librosa >= 0.6.2',
    'matplotlib >= 1.5.3',
    'mido == 1.2.6',
    'mir_eval >= 0.4',
    'numpy >= 1.14.6',  # 1.14.6 is required for colab compatibility.
    'pandas >= 0.18.1',
    'pretty_midi >= 0.2.6',
    'protobuf >= 3.6.1',
    'pygtrie >= 2.3',
    'python-rtmidi >= 1.1, < 1.2',  # 1.2 breaks us
    'scipy >= 0.18.1, <= 1.2.0',  # 1.2.1 causes segfaults in pytest.
    'sk-video',
    'sonnet',
    'sox >= 1.3.7',
    'tensorflow-datasets >= 1.0.2',
    'tensorflow-probability >= 0.5.0',
    'tensor2tensor >= 1.10.0',
    'wheel',
    'futures;python_version=="2.7"',
    'apache-beam[gcp] >= 2.8.0;python_version=="2.7"',
]

if gpu_mode:
  REQUIRED_PACKAGES.append('tensorflow-gpu >= 1.12.0')
else:
  REQUIRED_PACKAGES.append('tensorflow >= 1.12.0')

# pylint:disable=line-too-long
CONSOLE_SCRIPTS = [
    'magenta.interfaces.midi.magenta_midi',
    'magenta.interfaces.midi.midi_clock',
    'magenta.models.arbitrary_image_stylization.arbitrary_image_stylization_evaluate',
    'magenta.models.arbitrary_image_stylization.arbitrary_image_stylization_train',
    'magenta.models.arbitrary_image_stylization.arbitrary_image_stylization_with_weights',
    'magenta.models.arbitrary_image_stylization.arbitrary_image_stylization_distill_mobilenet',
    'magenta.models.drums_rnn.drums_rnn_create_dataset',
    'magenta.models.drums_rnn.drums_rnn_generate',
    'magenta.models.drums_rnn.drums_rnn_train',
    'magenta.models.image_stylization.image_stylization_create_dataset',
    'magenta.models.image_stylization.image_stylization_evaluate',
    'magenta.models.image_stylization.image_stylization_finetune',
    'magenta.models.image_stylization.image_stylization_train',
    'magenta.models.image_stylization.image_stylization_transform',
    'magenta.models.improv_rnn.improv_rnn_create_dataset',
    'magenta.models.improv_rnn.improv_rnn_generate',
    'magenta.models.improv_rnn.improv_rnn_train',
    'magenta.models.gansynth.gansynth_train',
    'magenta.models.gansynth.gansynth_generate',
    'magenta.models.melody_rnn.melody_rnn_create_dataset',
    'magenta.models.melody_rnn.melody_rnn_generate',
    'magenta.models.melody_rnn.melody_rnn_train',
    'magenta.models.music_vae.music_vae_generate',
    'magenta.models.music_vae.music_vae_train',
    'magenta.models.nsynth.wavenet.nsynth_generate',
    'magenta.models.nsynth.wavenet.nsynth_save_embeddings',
    'magenta.models.onsets_frames_transcription.onsets_frames_transcription_create_dataset_maps',
    'magenta.models.onsets_frames_transcription.onsets_frames_transcription_create_dataset_maestro',
    'magenta.models.onsets_frames_transcription.onsets_frames_transcription_infer',
    'magenta.models.onsets_frames_transcription.onsets_frames_transcription_train',
    'magenta.models.onsets_frames_transcription.onsets_frames_transcription_transcribe',
    'magenta.models.performance_rnn.performance_rnn_create_dataset',
    'magenta.models.performance_rnn.performance_rnn_generate',
    'magenta.models.performance_rnn.performance_rnn_train',
    'magenta.models.pianoroll_rnn_nade.pianoroll_rnn_nade_create_dataset',
    'magenta.models.pianoroll_rnn_nade.pianoroll_rnn_nade_generate',
    'magenta.models.pianoroll_rnn_nade.pianoroll_rnn_nade_train',
    'magenta.models.polyphony_rnn.polyphony_rnn_create_dataset',
    'magenta.models.polyphony_rnn.polyphony_rnn_generate',
    'magenta.models.polyphony_rnn.polyphony_rnn_train',
    'magenta.models.rl_tuner.rl_tuner_train',
    'magenta.models.sketch_rnn.sketch_rnn_train',
    'magenta.scripts.convert_dir_to_note_sequences',
    'magenta.tensor2tensor.t2t_datagen',
    'magenta.tensor2tensor.t2t_decoder',
    'magenta.tensor2tensor.t2t_trainer',
]
# pylint:enable=line-too-long

setup(
    name='magenta-gpu' if gpu_mode else 'magenta',
    version=__version__,  # pylint: disable=undefined-variable
    description='Use machine learning to create art and music',
    long_description='',
    url='https://magenta.tensorflow.org/',
    author='Google Inc.',
    author_email='magenta-discuss@gmail.com',
    license='Apache 2',
    # PyPI package information.
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='tensorflow machine learning magenta music art',

    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    entry_points={
        'console_scripts': ['%s = %s:console_entry_point' % (n, p) for n, p in
                            ((s.split('.')[-1], s) for s in CONSOLE_SCRIPTS)],
    },

    include_package_data=True,
    package_data={
        'magenta': ['models/image_stylization/evaluation_images/*.jpg'],
    },
    setup_requires=['pytest-runner', 'pytest-pylint'],
    tests_require=[
        'pytest',
        'pylint < 2.0.0;python_version<"3"',
        # pylint 2.3.0 and astroid 2.2.0 caused spurious errors,
        # so lock them down to known good versions.
        'pylint == 2.2.2;python_version>="3"',
        'astroid == 2.0.4;python_version>="3"',
    ],
)
