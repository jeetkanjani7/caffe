#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=examples/dogs_cats
DATA=data/dogs_cats
TOOLS=build/tools

$TOOLS/compute_image_mean $EXAMPLE/dogscats_train_lmdb \
  $DATA/dogscats_mean.binaryproto

echo "Done."
