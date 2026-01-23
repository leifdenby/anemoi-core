# Anemoi Classes With Config __init__ Arguments

Class inventory for anemoi graphs, models, and training modules, listing classes whose __init__ takes config-like arguments.
Built on 2026-01-23 08:49:30 , commit 27bd3dd.

Total classes: `85`

| Class | __init__ argument(s) | Module |
| --- | --- | --- |
| `AnemoiDatasetNodes` | `dataset: DictConfig` | `anemoi-graphs` |
| `GraphCreator` | `config: str \| Path \| DotDict \| DictConfig` | `anemoi-graphs` |
| `AnemoiDiffusionModelEncProcDec` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiDiffusionTendModelEncProcDec` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiEnsModelEncProcDec` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiModelEncProcDec` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiModelEncProcDecHierarchical` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiModelEncProcDecInterpolator` | `model_config: DotDict` | `anemoi-models` |
| `AnemoiModelInterface` | `config: DotDict` | `anemoi-models` |
| `BaseGraphModel` | `model_config: DotDict` | `anemoi-models` |
| `BaseImputer` | `config` | `anemoi-models` |
| `BaseMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `BasePreprocessor` | `config` | `anemoi-models` |
| `BaseProcessor` | `layer_kernels: DotDict` | `anemoi-models` |
| `ConditionalPostprocessor` | `config` | `anemoi-models` |
| `ConstantImputer` | `config` | `anemoi-models` |
| `CopyImputer` | `config` | `anemoi-models` |
| `DynamicConstantImputer` | `config` | `anemoi-models` |
| `DynamicCopyImputer` | `config` | `anemoi-models` |
| `DynamicInputImputer` | `config` | `anemoi-models` |
| `GNNBackwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GNNBaseMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GNNForwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GNNProcessor` | `layer_kernels: DotDict` | `anemoi-models` |
| `GNNProcessorChunk` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphConv` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphConvBaseBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerBackwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerBaseBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerBaseMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerForwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerMapperBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerProcessor` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerProcessorBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `GraphTransformerProcessorChunk` | `layer_kernels: DotDict` | `anemoi-models` |
| `IndexCollection` | `config` | `anemoi-models` |
| `InputImputer` | `config` | `anemoi-models` |
| `InputNormalizer` | `config` | `anemoi-models` |
| `MLP` | `layer_kernels: DotDict` | `anemoi-models` |
| `MultiHeadSelfAttention` | `layer_kernels: DotDict` | `anemoi-models` |
| `NoiseConditioning` | `layer_kernels: DotDict` | `anemoi-models` |
| `NoiseInjector` | `layer_kernels: DotDict` | `anemoi-models` |
| `NormalizedReluPostprocessor` | `config` | `anemoi-models` |
| `PointWiseMLPProcessor` | `layer_kernels: DotDict` | `anemoi-models` |
| `PointWiseMLPProcessorBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `PointWiseMLPProcessorChunk` | `layer_kernels: DotDict` | `anemoi-models` |
| `Postprocessor` | `config` | `anemoi-models` |
| `Remapper` | `config` | `anemoi-models` |
| `TransformerBackwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerBaseMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerForwardMapper` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerMapperBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerProcessor` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerProcessorBlock` | `layer_kernels: DotDict` | `anemoi-models` |
| `TransformerProcessorChunk` | `layer_kernels: DotDict` | `anemoi-models` |
| `AnemoiCheckpoint` | `config: OmegaConf` | `anemoi-training` |
| `AnemoiDatasetsDataModule` | `config: BaseSchema` | `anemoi-training` |
| `AnemoiProfiler` | `config: DictConfig` | `anemoi-training` |
| `AnemoiTrainer` | `config: DictConfig` | `anemoi-training` |
| `BaseGraphModule` | `config: BaseSchema` | `anemoi-training` |
| `BasePerBatchPlotCallback` | `config: OmegaConf` | `anemoi-training` |
| `BasePerEpochPlotCallback` | `config: OmegaConf` | `anemoi-training` |
| `BasePlotCallback` | `config: BaseSchema` | `anemoi-training` |
| `BenchmarkProfiler` | `config: DictConfig` | `anemoi-training` |
| `EarlyStopping` | `config: DictConfig` | `anemoi-training` |
| `EnsembleInitialConditions` | `config: DictConfig` | `anemoi-training` |
| `GeneralVariableLossScaler` | `weights: DictConfig` | `anemoi-training` |
| `GraphDiffusionForecaster` | `config: BaseSchema` | `anemoi-training` |
| `GraphDiffusionTendForecaster` | `config: BaseSchema` | `anemoi-training` |
| `GraphEnsForecaster` | `config: DictConfig` | `anemoi-training` |
| `GraphForecaster` | `config: BaseSchema` | `anemoi-training` |
| `GraphInterpolator` | `config: DictConfig` | `anemoi-training` |
| `GraphTrainableFeaturesPlot` | `config: OmegaConf`, `config: DictConfig` | `anemoi-training` |
| `LearningRateMonitor` | `config: DictConfig` | `anemoi-training` |
| `LongRolloutPlots` | `config: OmegaConf` | `anemoi-training` |
| `MemorySnapshotRecorder` | `config` | `anemoi-training` |
| `ParentUUIDCallback` | `config: OmegaConf` | `anemoi-training` |
| `PlotEnsSample` | `config: DictConfig` | `anemoi-training` |
| `PlotHistogram` | `config: OmegaConf`, `config: DictConfig` | `anemoi-training` |
| `PlotLoss` | `config: OmegaConf` | `anemoi-training` |
| `PlotSample` | `config: OmegaConf`, `config: DictConfig` | `anemoi-training` |
| `PlotSpectrum` | `config: OmegaConf`, `config: DictConfig` | `anemoi-training` |
| `RolloutEval` | `config: OmegaConf` | `anemoi-training` |
| `StochasticWeightAveraging` | `config: DictConfig` | `anemoi-training` |
| `TimeLimit` | `config: DictConfig` | `anemoi-training` |
