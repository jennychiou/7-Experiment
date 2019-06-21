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

"""Tests for infer_util."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from magenta.models.onsets_frames_transcription import infer_util
from magenta.protobuf import music_pb2

import numpy as np
import tensorflow as tf


class InferUtilTest(tf.test.TestCase):

  def testSequenceToValuedIntervals(self):
    sequence = music_pb2.NoteSequence()
    sequence.notes.add(pitch=60, start_time=1.0, end_time=2.0, velocity=80)
    # Should be dropped because it is 0 duration.
    sequence.notes.add(pitch=60, start_time=3.0, end_time=3.0, velocity=90)

    intervals, pitches, velocities = infer_util.sequence_to_valued_intervals(
        sequence)
    np.testing.assert_array_equal([[1., 2.]], intervals)
    np.testing.assert_array_equal([60], pitches)
    np.testing.assert_array_equal([80], velocities)


if __name__ == '__main__':
  tf.test.main()
