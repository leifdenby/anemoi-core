# What is this?

This directory contains a pyproject for training Anemoi LAM models. It is based off the Anemoi Core `graphs`, `models`, and `training` packages.


## Getting started

To get started, clone this repository, install [uv]() and ensure you can run `anemoi`'s training CLI commands:

```bash
$> uv run anemoi.training --help

usage: anemoi-training train [-h]

Commands to train Anemoi models.

options:
  -h, --help  show this help message and exit
```

> TODO: raise issue to improve help message

That command in itself doesn't give you much help, but if you pass different commandline arguments you can see more:

```bash
$> uv run anemoi.training --config
2026-02-03 12:06:14 INFO Running anemoi training command with overrides: ['--config', 'lam']
usage: .anemoi-training-train [--help] [--hydra-help] [--version] [--cfg {job,hydra,all}] [--resolve] [--package PACKAGE] [--run] [--multirun]
                              [--shell-completion] [--config-path CONFIG_PATH] [--config-name CONFIG_NAME] [--config-dir CONFIG_DIR]
                              [--experimental-rerun EXPERIMENTAL_RERUN] [--info [{all,config,defaults,defaults-tree,plugins,searchpath}]]
                              [overrides ...]
.anemoi-training-train: error: ambiguous option: --config could match --config-path, --config-name, --config-dir
```

> TODO: raise issue to understand why using `--config-path` doesn't work here

The configs have to reside in `training/src/anemoi/training/config`, and must
be referenced by the "name" of the config. We will use the `lam` config for
training Anemoi LAM models, i.e. the yaml config file in
`training/src/anemoi/training/config/lam.yaml`.


## Creating a ERA5 subset dataset for testing

To create a small subset of the ERA5 dataset for testing we use `anemoi-datasets create` CLI call passing in a config yaml-file that uses the original ERA5 dataset as input and specifies a small time-range and selects only a few variables:

```yaml
name: era5-o96-1990-09-6h-subset-v1
description: ERA5 O96 dataset for September 1990 only
attribution: ECMWF/C3S  
licence: CC-BY-4.0  
  
dates:  
  start: "1990-09-01T00:00:00"  
  end: "1990-09-30T18:00:00"  
  frequency: 6h  
  
input:  
  anemoi-dataset:  
    dataset: "https://data.ecmwf.int/anemoi-datasets/era5-o96-1979-2023-6h-v8.zarr"  
    params: ["2t", "msl", "sp", "10u", "10v"]  
  
statistics:  
  end: 1990  
  
checks: []
```

the `input.anemoi-dataset` is important here since the key `anemoi-dataset`
tells the `anemoi-datasets` CLI that were trying to read what is already an
Anemoi Dataset. The path to the original ERA5 dataset is given in the `dataset`
field.

Create using the following command:

```bash
$> uv run anemoi-datasets create era5-sep-1990-subset.yaml ~/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr --overwrite

2026-02-03 12:37:10 INFO 🎬 Task init((),{}) starting
2026-02-03 12:37:10 INFO Setting flatten_grid=True in config
2026-02-03 12:37:10 INFO Setting ensemble_dimension=2 in config
2026-02-03 12:37:10 INFO Setting flatten_grid=True in config
2026-02-03 12:37:10 INFO Setting ensemble_dimension=2 in config
2026-02-03 12:37:10 INFO {'start': '1990-09-01T00:00:00', 'end': '1990-09-30T18:00:00', 'frequency': '6h', 'group_by': 'monthly'}
2026-02-03 12:37:10 INFO Groups(dates=1,StartEndDates(1990-09-01 00:00:00..1990-09-30 18:00:00 every 6:00:00))
2026-02-03 12:37:10 INFO Groups: Groups(dates=1,StartEndDates(1990-09-01 00:00:00..1990-09-30 18:00:00 every 6:00:00))
dict_keys(['valid_datetime', 'latitudes', 'longitudes', 'param', 'values'])
2026-02-03 12:37:19 INFO Registering data at path: ('input', 'anemoi-dataset')
2026-02-03 12:37:19 INFO Minimal input for 'init' step (using only the first date) : GroupOfDates(dates=['1990-09-01T00:00:00'])
2026-02-03 12:37:19 INFO <anemoi.datasets.create.input.result.field.FieldResult object at 0xee8426d48c80>
2026-02-03 12:37:19 INFO Config loaded ok:
2026-02-03 12:37:19 INFO Found 120 datetimes.
2026-02-03 12:37:19 INFO Dates: Found 120 datetimes, in 1 groups:
2026-02-03 12:37:19 INFO Missing dates: 0
2026-02-03 12:37:19 INFO Found 5 variables : 10u,10v,2t,msl,sp.
2026-02-03 12:37:19 INFO Found 1 ensembles : 0.
2026-02-03 12:37:19 INFO gridpoints size: [40320, 40320]
2026-02-03 12:37:19 INFO resolution=None
2026-02-03 12:37:19 INFO total_shape = [120, 5, 1, 40320]
2026-02-03 12:37:19 INFO chunks=(1, 5, 1, 40320)
2026-02-03 12:37:19 INFO Creating Dataset '/home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr', with total_shape=[120, 5, 1, 40320], chunks=(1, 5, 1, 40320) and dtype='float32'
2026-02-03 12:37:19 WARNING Dataset name error: the dataset name 'era5-o96-1990-09-6h-subset-v1' does not follow naming convention. Does not match ^(\w+)-([\w-]+)-(\w+)-(\w+)-(\d\d\d\d)-(\d\d\d\d)-(\d+h|\d+m)-v(\d+)-?([a-zA-Z0-9-]+)?$
2026-02-03 12:37:19 INFO Number of years 0 < 10, leaving out 20%. end=numpy.datetime64('1990-09-24T18:00:00')
2026-02-03 12:37:19 INFO Will compute statistics from 1990-09-01T00:00:00 to 1990-09-30T18:00:00
2026-02-03 12:37:19 INFO 🏁 Task init((),{}) completed (0:00:08.899896)
2026-02-03 12:37:19 INFO 🎬 Task load((),{}) starting
2026-02-03 12:37:19 INFO {'end': '1990-09-30T18:00:00', 'frequency': '6h', 'group_by': 'monthly', 'start': '1990-09-01T00:00:00'}
2026-02-03 12:37:19 INFO Groups(dates=1,StartEndDates(1990-09-01 00:00:00..1990-09-30 18:00:00 every 6:00:00))
dict_keys(['valid_datetime', 'latitudes', 'longitudes', 'param', 'values'])
2026-02-03 12:42:32 INFO Registering data at path: ('input', 'anemoi-dataset')
2026-02-03 12:42:32 INFO Loading array shape=(120, 5, 1, 40320), indexes=120
Loading 599/600: 100%|████████████████████████████████████████████████████████████████████████████████████████| 600/600 [00:00<00:00, 19922.12it/s]
2026-02-03 12:42:32 INFO Computing statistics for (120, 5, 1, 40320) array
2026-02-03 12:42:32 INFO Statistics computed for 5 variables.
2026-02-03 12:42:32 INFO Flush data array
2026-02-03 12:42:32 INFO Flushed data array
2026-02-03 12:42:33 INFO Name               : /data
Type               : zarr.core.Array
Data type          : float32
Shape              : (120, 5, 1, 40320)
Chunk shape        : (1, 5, 1, 40320)
Order              : C
Read-only          : True
Compressor         : Blosc(cname='lz4', clevel=5, shuffle=SHUFFLE, blocksize=0)
Store type         : zarr.storage.DirectoryStore
No. bytes          : 96768000 (92.3M)
No. bytes stored   : 59425093 (56.7M)
Storage ratio      : 1.6
Chunks initialized : 120/120

2026-02-03 12:42:33 INFO 🏁 Task load((),{}) completed (0:05:14.655019)
2026-02-03 12:42:33 INFO 🎬 Task finalise((),{}) starting
2026-02-03 12:42:33 INFO Variables minimum maximum mean stdev has_nans
10u -32.22 28.91 -0.34 5.38 0.00
10v -26.71 31.83 0.62 4.47 0.00
2t 195.24 319.30 288.89 14.97 0.00
msl 92596.50 104111.81 101137.58 1151.57 0.00
sp 51574.79 104095.31 98566.24 6906.70 0.00
2026-02-03 12:42:33 INFO Wrote statistics in /home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr
Computing size of /home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr: 16it [00:00, 18436.50it/s]
2026-02-03 12:42:33 INFO Total size: 56.8 MiB
2026-02-03 12:42:33 INFO Total number of files: 166
2026-02-03 12:42:33 INFO 🏁 Task finalise((),{}) completed (0:00:00.030458)
2026-02-03 12:42:33 INFO 🎬 Task init_additions((),{}) starting
2026-02-03 12:42:33 WARNING No delta found in kwargs, no additions will be computed.
2026-02-03 12:42:33 INFO 🏁 Task init_additions((),{}) completed (0:00:00.000108)
2026-02-03 12:42:33 INFO 🎬 Task load_additions((),{}) starting
2026-02-03 12:42:33 WARNING No delta found in kwargs, no additions will be computed.
2026-02-03 12:42:33 INFO 🏁 Task load_additions((),{}) completed (0:00:00.000069)
2026-02-03 12:42:33 INFO 🎬 Task finalise_additions((),{}) starting
2026-02-03 12:42:33 WARNING No delta found in kwargs, no additions will be computed.
Computing size of /home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr: 13it [00:00, 18821.52it/s]
2026-02-03 12:42:33 INFO Total size: 56.8 MiB
2026-02-03 12:42:33 INFO Total number of files: 159
2026-02-03 12:42:33 INFO 🏁 Task finalise_additions((),{}) completed (0:00:00.009025)
2026-02-03 12:42:33 INFO 🎬 Task patch((),{}) starting
2026-02-03 12:42:33 INFO ✅ Remove _create_yaml_config
2026-02-03 12:42:33 INFO Dataset changed by patch
2026-02-03 12:42:33 INFO 🏁 Task patch((),{}) completed (0:00:00.020636)
2026-02-03 12:42:33 INFO 🎬 Task cleanup((),{}) starting
2026-02-03 12:42:33 INFO 🏁 Task cleanup((),{}) completed (0:00:00.000103)
2026-02-03 12:42:33 INFO 🎬 Task verify((),{}) starting
2026-02-03 12:42:33 INFO Verifying dataset at /home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr
2026-02-03 12:42:33 INFO /home/lcd/anemoi-datasets/era5-o96-1990-09-6h-subset-v1.zarr
2026-02-03 12:42:33 INFO 🏁 Task verify((),{}) completed (0:00:00.000216)
2026-02-03 12:42:33 INFO Create completed in 5 minutes 23 seconds
```

> TODO: work out why the statistics are being computed over the full time-range and not just up to 1990-09-24 as expected (the last 20% being held out for validation)


## Starting training

Foot guns:

- Paths to datasets can't start with `~`, have to be full paths. The exception message given is `Attribute` error when trying to access `self.z.data` in `anemoi.datasets.data.stores`.


Outstanding issues:

- setting `dataloader.[training,validation,test].frequency` causes an issue when opening the dataset saying that the validation dataset only has one timestep (1990-09-30), but that isn't right. Without this training runs, but that doesn't make sense ERA5 is at 6hr resolution and DANRA is at 3hr.

Start training using:

```bash
$> ANEMOI_BASE_SEED=42 uv run anemoi-training train --config-name lam
```