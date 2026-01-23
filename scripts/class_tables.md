# Anemoi Class Inventory

Class inventory for anemoi graphs, models, and training modules, listing base/derived classes, files, and markers for abstract and torch module inheritance.

Built on 23/1/2026, from commit [27bd3dd](https://github.com/ecmwf/anemoi-core/commit/27bd3dd) committed 10/10/2025

Table of contents:

| Module | Base count | Non-base count |
| --- | --- | --- |
| [anemoi-graphs](#anemoi-graphs) | 89 | 42 |
| [anemoi-models](#anemoi-models) | 74 | 104 |
| [anemoi-training](#anemoi-training) | 84 | 120 |

## anemoi-graphs
Base classes (no explicit base or ABC-derived): 89
| Class | File |
| --- | --- |
| AnemoiDatasetNodes* | graphs/src/anemoi/graphs/nodes/builders/from_file.py |
| AttributeFromSourceNode* | graphs/src/anemoi/graphs/edges/attributes.py |
| AttributeFromTargetNode* | graphs/src/anemoi/graphs/edges/attributes.py |
| Azimuth* | graphs/src/anemoi/graphs/edges/attributes.py |
| BaseAnemoiDatasetVariable* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| BaseAreaWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| BaseBooleanEdgeAttributeBuilder* | graphs/src/anemoi/graphs/edges/attributes.py |
| BaseCombineAnemoiDatasetsMask* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| BaseDistanceEdgeBuilders* | graphs/src/anemoi/graphs/edges/builders/base.py |
| BaseEdgeAttributeBuilder* | graphs/src/anemoi/graphs/edges/attributes.py |
| BaseEdgeAttributeFromNodeBuilder* | graphs/src/anemoi/graphs/edges/attributes.py |
| BaseEdgeBuilder* | graphs/src/anemoi/graphs/edges/builders/base.py |
| BaseEdgeMaskingProcessor* | graphs/src/anemoi/graphs/processors/post_process.py |
| BaseIcosahedronEdgeStrategy* | graphs/src/anemoi/graphs/generate/multi_scale_edges.py |
| BaseLatWeightedAttribute* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| BaseNodeAttribute* | graphs/src/anemoi/graphs/nodes/attributes/base_attributes.py |
| BaseNodeBuilder* | graphs/src/anemoi/graphs/nodes/builders/base.py |
| BaseNodeMaskingProcessor* | graphs/src/anemoi/graphs/processors/post_process.py |
| BasePositionalBuilder* | graphs/src/anemoi/graphs/edges/attributes.py |
| BaseSortEdgeIndex* | graphs/src/anemoi/graphs/processors/post_process.py |
| BipartiteGraph | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| BooleanAndMask* | graphs/src/anemoi/graphs/nodes/attributes/boolean_op.py |
| BooleanBaseNodeAttribute* | graphs/src/anemoi/graphs/nodes/attributes/base_attributes.py |
| BooleanNot* | graphs/src/anemoi/graphs/nodes/attributes/boolean_op.py |
| BooleanOperation* | graphs/src/anemoi/graphs/nodes/attributes/boolean_op.py |
| BooleanOrMask* | graphs/src/anemoi/graphs/nodes/attributes/boolean_op.py |
| CosineLatWeightedAttribute* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| CutOffEdges* | graphs/src/anemoi/graphs/edges/builders/cutoff.py |
| CutOutMask* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| DirectionalHarmonics* | graphs/src/anemoi/graphs/edges/attributes.py |
| EdgeDirection* | graphs/src/anemoi/graphs/edges/attributes.py |
| EdgeID | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| EdgeLength* | graphs/src/anemoi/graphs/edges/attributes.py |
| GaussianDistanceWeights* | graphs/src/anemoi/graphs/edges/attributes.py |
| GeneralGraph | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| GraphCreator | graphs/src/anemoi/graphs/create.py |
| GraphDescriptor | graphs/src/anemoi/graphs/describe.py |
| GraphExporter | graphs/src/anemoi/graphs/export.py |
| GraphInspector | graphs/src/anemoi/graphs/inspect.py |
| GridsMask* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| HEALPixNodes* | graphs/src/anemoi/graphs/nodes/builders/from_healpix.py |
| HexNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| HexNodesEdgeBuilder* | graphs/src/anemoi/graphs/generate/multi_scale_edges.py |
| ICONCellGridNodes* | graphs/src/anemoi/graphs/nodes/builders/from_icon.py |
| ICONMultimeshNodes* | graphs/src/anemoi/graphs/nodes/builders/from_icon.py |
| ICONNodes* | graphs/src/anemoi/graphs/nodes/builders/from_icon.py |
| ICONTopologicalBaseEdgeBuilder* | graphs/src/anemoi/graphs/edges/builders/icon.py |
| ICONTopologicalBaseNodeBuilder* | graphs/src/anemoi/graphs/nodes/builders/from_icon.py |
| ICONTopologicalDecoderEdges* | graphs/src/anemoi/graphs/edges/builders/icon.py |
| ICONTopologicalEncoderEdges* | graphs/src/anemoi/graphs/edges/builders/icon.py |
| ICONTopologicalProcessorEdges* | graphs/src/anemoi/graphs/edges/builders/icon.py |
| IcosahedralNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| IsolatitudeAreaWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| KNNAreaMaskBuilder | graphs/src/anemoi/graphs/generate/masks.py |
| KNNEdges* | graphs/src/anemoi/graphs/edges/builders/knn.py |
| LatLonNodes* | graphs/src/anemoi/graphs/nodes/builders/from_vectors.py |
| LimitedAreaHEALPixNodes* | graphs/src/anemoi/graphs/nodes/builders/from_healpix.py |
| LimitedAreaHexNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| LimitedAreaIcosahedralNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| LimitedAreaNPZFileNodes* | graphs/src/anemoi/graphs/nodes/builders/from_file.py |
| LimitedAreaTriNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| MaskedPlanarAreaWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| MultiScaleEdges* | graphs/src/anemoi/graphs/edges/builders/multi_scale.py |
| NodeMaskingMixin | graphs/src/anemoi/graphs/edges/builders/masking.py |
| NodeSet | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| NonmissingAnemoiDatasetVariable* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| NonzeroAnemoiDatasetVariable* | graphs/src/anemoi/graphs/nodes/attributes/masks.py |
| NormaliserMixin | graphs/src/anemoi/graphs/normalise.py |
| NPZFileNodes* | graphs/src/anemoi/graphs/nodes/builders/from_file.py |
| PlanarAreaWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| PostProcessor* | graphs/src/anemoi/graphs/processors/post_process.py |
| RadialBasisFeatures* | graphs/src/anemoi/graphs/edges/attributes.py |
| ReducedGaussianGridNodes* | graphs/src/anemoi/graphs/nodes/builders/from_reduced_gaussian.py |
| RemoveUnconnectedNodes* | graphs/src/anemoi/graphs/processors/post_process.py |
| RestrictEdgeLength* | graphs/src/anemoi/graphs/processors/post_process.py |
| ReversedCutOffEdges* | graphs/src/anemoi/graphs/edges/builders/cutoff.py |
| ReversedKNNEdges* | graphs/src/anemoi/graphs/edges/builders/knn.py |
| SortEdgeIndexBySourceNodes* | graphs/src/anemoi/graphs/processors/post_process.py |
| SortEdgeIndexByTargetNodes* | graphs/src/anemoi/graphs/processors/post_process.py |
| SphericalAreaWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| StretchedIcosahedronNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| StretchedTriNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| StretchedTriNodesEdgeBuilder* | graphs/src/anemoi/graphs/generate/multi_scale_edges.py |
| SubsetNodesInArea* | graphs/src/anemoi/graphs/processors/post_process.py |
| TextNodes* | graphs/src/anemoi/graphs/nodes/builders/from_file.py |
| TriNodes* | graphs/src/anemoi/graphs/nodes/builders/from_refined_icosahedron.py |
| TriNodesEdgeBuilder* | graphs/src/anemoi/graphs/generate/multi_scale_edges.py |
| UniformWeights* | graphs/src/anemoi/graphs/nodes/attributes/area_weights.py |
| XArrayNodes* | graphs/src/anemoi/graphs/nodes/builders/from_file.py |

* indicates abstract base class (derives from ABC).

Derived classes (explicit base list): 42
| Class | Base(s) | File |
| --- | --- | --- |
| AnemoiDatasetNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| BaseEdgeAttributeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_attributes_schemas.py |
| BaseGraphSchema | PydanticBaseModel | graphs/src/anemoi/graphs/schemas/base_graph.py |
| BooleanOperationSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| Create | Command | graphs/src/anemoi/graphs/commands/create.py |
| CutoffEdgeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_schemas.py |
| CutOutMaskSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| Describe | Command | graphs/src/anemoi/graphs/commands/describe.py |
| DirectionalHarmonicsSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_attributes_schemas.py |
| EdgeAttributeFromNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_attributes_schemas.py |
| EdgeAttributeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_schemas.py |
| EdgeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/base_graph.py |
| ExportToSparse | Command | graphs/src/anemoi/graphs/commands/export_to_sparse.py |
| GridsMaskSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| ICONCellDataGrid | BipartiteGraph | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| ICONMeshNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| ICONMultiMesh | GeneralGraph | graphs/src/anemoi/graphs/generate/icon_mesh.py |
| ICONNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| ICONTopologicalEdgeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_schemas.py |
| IcosahedralandHealPixNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| ImplementedEdgeAttributeSchema | str, Enum | graphs/src/anemoi/graphs/schemas/edge_attributes_schemas.py |
| Inspect | Command | graphs/src/anemoi/graphs/commands/inspect.py |
| KNNEdgeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_schemas.py |
| LimitedAreaIcosahedralandHealPixNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| LimitedAreaNPZFileNodesSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| MaskedPlanarAreaWeightsSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| MultiScaleEdgeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_schemas.py |
| NodesAxis | Enum | graphs/src/anemoi/graphs/utils.py |
| NodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/base_graph.py |
| NonmissingAnemoiDatasetVariableSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| NPZnodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| PlanarAreaWeightSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| RadialBasisFeaturesSchema | BaseModel | graphs/src/anemoi/graphs/schemas/edge_attributes_schemas.py |
| ReducedGaussianGridNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| RemoveUnconnectedNodesSchema | BaseModel | graphs/src/anemoi/graphs/schemas/post_processors.py |
| RestrictEdgeLengthSchema | BaseModel | graphs/src/anemoi/graphs/schemas/post_processors.py |
| SortEdgeIndexSchema | BaseModel | graphs/src/anemoi/graphs/schemas/post_processors.py |
| SphericalAreaWeightSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_attributes_schemas.py |
| StretchedIcosahdralNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| SubsetNodesInAreaSchema | BaseModel | graphs/src/anemoi/graphs/schemas/post_processors.py |
| TextNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |
| XArrayNodeSchema | BaseModel | graphs/src/anemoi/graphs/schemas/node_schemas.py |

## anemoi-models
Base classes (no explicit base or ABC-derived): 74
| Class | File |
| --- | --- |
| _SerializedRollback | models/src/anemoi/models/migrations/migrator.py |
| BackwardMapperPostProcessMixin | models/src/anemoi/models/layers/mapper.py |
| BaseBlock*† | models/src/anemoi/models/layers/block.py |
| BaseBounding*† | models/src/anemoi/models/layers/bounding.py |
| BaseImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| BaseIndex | models/src/anemoi/models/data_indices/index.py |
| BaseMapper*† | models/src/anemoi/models/layers/mapper.py |
| BaseOp | models/src/anemoi/models/migrations/migrator.py |
| BaseProcessor*† | models/src/anemoi/models/layers/processor.py |
| BaseProcessorChunk*† | models/src/anemoi/models/layers/chunk.py |
| BaseTensorIndex | models/src/anemoi/models/data_indices/tensor.py |
| BaseTruncation | models/src/anemoi/models/layers/truncation.py |
| Config | models/src/anemoi/models/schemas/common_components.py |
| ConstantImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| CopyImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| CosineScheduler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| DeserializeMigrationContext | models/src/anemoi/models/migrations/setup_context.py |
| DiffusionSampler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| DPMpp2MSampler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| DynamicConstantImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| DynamicCopyImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| DynamicInputImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| DynamicMixin | models/src/anemoi/models/preprocessing/imputer.py |
| EDMHeunSampler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| ExponentialScheduler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| ForwardMapperPreProcessMixin | models/src/anemoi/models/layers/mapper.py |
| FractionBounding*† | models/src/anemoi/models/layers/bounding.py |
| GNNBackwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| GNNBaseMapper*† | models/src/anemoi/models/layers/mapper.py |
| GNNForwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| GNNProcessor*† | models/src/anemoi/models/layers/processor.py |
| GNNProcessorChunk*† | models/src/anemoi/models/layers/chunk.py |
| GraphConvBaseBlock*† | models/src/anemoi/models/layers/block.py |
| GraphConvMapperBlock*† | models/src/anemoi/models/layers/block.py |
| GraphConvProcessorBlock*† | models/src/anemoi/models/layers/block.py |
| GraphEdgeMixin | models/src/anemoi/models/layers/mapper.py |
| GraphTransformerBackwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| GraphTransformerBaseBlock*† | models/src/anemoi/models/layers/block.py |
| GraphTransformerBaseMapper*† | models/src/anemoi/models/layers/mapper.py |
| GraphTransformerForwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| GraphTransformerMapperBlock*† | models/src/anemoi/models/layers/block.py |
| GraphTransformerProcessor*† | models/src/anemoi/models/layers/processor.py |
| GraphTransformerProcessorBlock*† | models/src/anemoi/models/layers/block.py |
| GraphTransformerProcessorChunk*† | models/src/anemoi/models/layers/chunk.py |
| HardtanhBounding*† | models/src/anemoi/models/layers/bounding.py |
| IndexCollection | models/src/anemoi/models/data_indices/collection.py |
| InputImputer*† | models/src/anemoi/models/preprocessing/imputer.py |
| KarrasScheduler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| LeakyFractionBounding*† | models/src/anemoi/models/layers/bounding.py |
| LeakyHardtanhBounding*† | models/src/anemoi/models/layers/bounding.py |
| LeakyReluBounding*† | models/src/anemoi/models/layers/bounding.py |
| LinearScheduler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| Migration | models/src/anemoi/models/migrations/migrator.py |
| MigrationContext | models/src/anemoi/models/migrations/setup_context.py |
| MigrationMetadata | models/src/anemoi/models/migrations/migrator.py |
| Migrator | models/src/anemoi/models/migrations/migrator.py |
| MissingAttribute | models/src/anemoi/models/migrations/migrator.py |
| NoiseScheduler* | models/src/anemoi/models/samplers/diffusion_samplers.py |
| NormalizedLeakyReluBounding*† | models/src/anemoi/models/layers/bounding.py |
| NormalizedReluBounding*† | models/src/anemoi/models/layers/bounding.py |
| PointWiseMLPProcessor*† | models/src/anemoi/models/layers/processor.py |
| PointWiseMLPProcessorBlock*† | models/src/anemoi/models/layers/block.py |
| PointWiseMLPProcessorChunk*† | models/src/anemoi/models/layers/chunk.py |
| ReluBounding*† | models/src/anemoi/models/layers/bounding.py |
| ReversedSetupCallback | models/src/anemoi/models/migrations/setup_context.py |
| SaveCkpt | models/src/anemoi/models/migrations/migrator.py |
| TransformerBackwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| TransformerBaseMapper*† | models/src/anemoi/models/layers/mapper.py |
| TransformerForwardMapper*† | models/src/anemoi/models/layers/mapper.py |
| TransformerMapperBlock*† | models/src/anemoi/models/layers/block.py |
| TransformerProcessor*† | models/src/anemoi/models/layers/processor.py |
| TransformerProcessorBlock*† | models/src/anemoi/models/layers/block.py |
| TransformerProcessorChunk*† | models/src/anemoi/models/layers/chunk.py |
| UnpicklerWrapper | models/src/anemoi/models/migrations/migrator.py |

> `*` indicates abstract base class (derives from ABC).  
> `†` indicates class derives from ABC and torch.nn.Module.

Derived from torch.nn.Module (direct or indirect): 36
| Class | Base(s) | File |
| --- | --- | --- |
| AnemoiDiffusionModelEncProcDec | BaseGraphModel | models/src/anemoi/models/models/diffusion_encoder_processor_decoder.py |
| AnemoiDiffusionTendModelEncProcDec | AnemoiDiffusionModelEncProcDec | models/src/anemoi/models/models/diffusion_encoder_processor_decoder.py |
| AnemoiEnsModelEncProcDec | AnemoiModelEncProcDec | models/src/anemoi/models/models/ens_encoder_processor_decoder.py |
| AnemoiModelEncProcDec | BaseGraphModel | models/src/anemoi/models/models/encoder_processor_decoder.py |
| AnemoiModelEncProcDecHierarchical | AnemoiModelEncProcDec | models/src/anemoi/models/models/hierarchical.py |
| AnemoiModelEncProcDecInterpolator | AnemoiModelEncProcDec | models/src/anemoi/models/models/interpolator.py |
| AnemoiModelInterface | torch.nn.Module | models/src/anemoi/models/interface/__init__.py |
| BaseGraphModel | nn.Module | models/src/anemoi/models/models/base.py |
| BasePreprocessor | nn.Module | models/src/anemoi/models/preprocessing/__init__.py |
| CheckpointWrapper | nn.Module | models/src/anemoi/models/layers/utils.py |
| ConditionalLayerNorm | nn.Module | models/src/anemoi/models/layers/normalization.py |
| ConditionalNaNPostprocessor | ConditionalPostprocessor | models/src/anemoi/models/preprocessing/postprocessor.py |
| ConditionalPostprocessor | Postprocessor | models/src/anemoi/models/preprocessing/postprocessor.py |
| ConditionalZeroPostprocessor | ConditionalPostprocessor | models/src/anemoi/models/preprocessing/postprocessor.py |
| CustomRelu | nn.Module | models/src/anemoi/models/layers/activations.py |
| FlashAttentionWrapper | nn.Module | models/src/anemoi/models/layers/attention.py |
| GEGLU | GLU | models/src/anemoi/models/layers/activations.py |
| GLU | nn.Module | models/src/anemoi/models/layers/activations.py |
| InputNormalizer | BasePreprocessor | models/src/anemoi/models/preprocessing/normalizer.py |
| MLP | nn.Module | models/src/anemoi/models/layers/mlp.py |
| MultiHeadCrossAttention | MultiHeadSelfAttention | models/src/anemoi/models/layers/attention.py |
| MultiHeadSelfAttention | nn.Module | models/src/anemoi/models/layers/attention.py |
| NamedNodesAttributes | nn.Module | models/src/anemoi/models/layers/graph.py |
| NoiseConditioning | NoiseInjector | models/src/anemoi/models/layers/ensemble.py |
| NoiseInjector | nn.Module | models/src/anemoi/models/layers/ensemble.py |
| NormalizedReluPostprocessor | Postprocessor | models/src/anemoi/models/preprocessing/postprocessor.py |
| Postprocessor | BasePreprocessor | models/src/anemoi/models/preprocessing/postprocessor.py |
| Processors | nn.Module | models/src/anemoi/models/preprocessing/__init__.py |
| RandomFourierEmbeddings | torch.nn.Module | models/src/anemoi/models/layers/diffusion.py |
| ReGLU | GLU | models/src/anemoi/models/layers/activations.py |
| Remapper | BasePreprocessor | models/src/anemoi/models/preprocessing/remapper.py |
| SDPAAttentionWrapper | nn.Module | models/src/anemoi/models/layers/attention.py |
| Sine | nn.Module | models/src/anemoi/models/layers/activations.py |
| SinusoidalEmbeddings | torch.nn.Module | models/src/anemoi/models/layers/diffusion.py |
| SwiGLU | GLU | models/src/anemoi/models/layers/activations.py |
| TrainableTensor | nn.Module | models/src/anemoi/models/layers/graph.py |

> `†` indicates class derives from ABC and torch.nn.Module.

Other derived classes (explicit base list): 68
| Class | Base(s) | File |
| --- | --- | --- |
| _GatherChannelsParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _GatherParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _ReduceParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _ReduceShardParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _ShardParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _SplitChannelsParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _SplitHeadsParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/transformer.py |
| _SplitSequenceParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/transformer.py |
| _SyncParallelSection | torch.autograd.Function | models/src/anemoi/models/distributed/graph.py |
| _Unpickler | Unpickler | models/src/anemoi/models/migrations/migrator.py |
| AutocastLayerNorm | nn.LayerNorm | models/src/anemoi/models/layers/normalization.py |
| BaseModelSchema | PydanticBaseModel | models/src/anemoi/models/schemas/models.py |
| Boolean1DSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| ConditionalNaNPostprocessorSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| ConditionalZeroPostprocessorSchema | RootModel[dict[Any, Any]] | models/src/anemoi/models/schemas/data_processor.py |
| ConstantImputerSchema | RootModel[dict[Any, Any]] | models/src/anemoi/models/schemas/data_processor.py |
| DataIndex | BaseIndex | models/src/anemoi/models/data_indices/index.py |
| DefinedModels | str, Enum | models/src/anemoi/models/schemas/models.py |
| DiffusionModel | Model | models/src/anemoi/models/schemas/models.py |
| DiffusionModelSchema | BaseModelSchema | models/src/anemoi/models/schemas/models.py |
| DiffusionSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| EnsModelSchema | BaseModelSchema | models/src/anemoi/models/schemas/models.py |
| FractionBoundingSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| GNNDecoderSchema | GNNModelComponent | models/src/anemoi/models/schemas/decoder.py |
| GNNEncoderSchema | GNNModelComponent | models/src/anemoi/models/schemas/encoder.py |
| GNNModelComponent | BaseModel | models/src/anemoi/models/schemas/common_components.py |
| GNNProcessorSchema | GNNModelComponent | models/src/anemoi/models/schemas/processor.py |
| GraphConv | MessagePassing | models/src/anemoi/models/layers/conv.py |
| GraphTransformerConv | MessagePassing | models/src/anemoi/models/layers/conv.py |
| GraphTransformerDecoderSchema | TransformerModelComponent | models/src/anemoi/models/schemas/decoder.py |
| GraphTransformerEncoderSchema | TransformerModelComponent | models/src/anemoi/models/schemas/encoder.py |
| GraphTransformerProcessorSchema | TransformerModelComponent | models/src/anemoi/models/schemas/processor.py |
| HardtanhBoundingSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| Hello | Command | models/src/anemoi/models/commands/hello.py |
| HierarchicalModelSchema | BaseModelSchema | models/src/anemoi/models/schemas/models.py |
| ImputerSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| IncompatibleCheckpointException | BaseException | models/src/anemoi/models/migrations/migrator.py |
| IncompleteMigrationScript | BaseException | models/src/anemoi/models/migrations/migrator.py |
| InputTensorIndex | BaseTensorIndex | models/src/anemoi/models/data_indices/tensor.py |
| LeakyFractionBoundingSchema | FractionBoundingSchema | models/src/anemoi/models/schemas/models.py |
| LeakyHardtanhBoundingSchema | HardtanhBoundingSchema | models/src/anemoi/models/schemas/models.py |
| LeakyReluBoundingSchema | ReluBoundingSchema | models/src/anemoi/models/schemas/models.py |
| Migration | Command | models/src/anemoi/models/commands/migration.py |
| MigrationOp | BaseOp | models/src/anemoi/models/migrations/migrator.py |
| Model | BaseModel | models/src/anemoi/models/schemas/models.py |
| ModelIndex | BaseIndex | models/src/anemoi/models/data_indices/index.py |
| NoiseInjectorSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| NoOutputMaskSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| NormalizedLeakyReluBoundingSchema | NormalizedReluBoundingSchema | models/src/anemoi/models/schemas/models.py |
| NormalizedReluBoundingSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| NormalizedReluPostprocessorSchema | RootModel[dict[Any, Any]] | models/src/anemoi/models/schemas/data_processor.py |
| NormalizerSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| OutputTensorIndex | BaseTensorIndex | models/src/anemoi/models/data_indices/tensor.py |
| PointWiseMLPProcessorSchema | PointWiseModelComponent | models/src/anemoi/models/schemas/processor.py |
| PointWiseModelComponent | BaseModel | models/src/anemoi/models/schemas/common_components.py |
| PostprocessorSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| PreprocessorSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| PreprocessorTarget | str, Enum | models/src/anemoi/models/schemas/data_processor.py |
| ReluBoundingSchema | BaseModel | models/src/anemoi/models/schemas/models.py |
| RemapperSchema | BaseModel | models/src/anemoi/models/schemas/data_processor.py |
| RollbackOp | BaseOp | models/src/anemoi/models/migrations/migrator.py |
| SerializedMigration | TypedDict | models/src/anemoi/models/migrations/migrator.py |
| SerializedMigrationContext | TypedDict | models/src/anemoi/models/migrations/setup_context.py |
| TrainableParameters | PydanticBaseModel | models/src/anemoi/models/schemas/models.py |
| TransformerDecoderSchema | TransformerModelComponent | models/src/anemoi/models/schemas/decoder.py |
| TransformerEncoderSchema | TransformerModelComponent | models/src/anemoi/models/schemas/encoder.py |
| TransformerModelComponent | PydanticBaseModel | models/src/anemoi/models/schemas/common_components.py |
| TransformerProcessorSchema | TransformerModelComponent | models/src/anemoi/models/schemas/processor.py |

## anemoi-training
Base classes (no explicit base or ABC-derived): 84
| Class | File |
| --- | --- |
| AlmostFairKernelCRPS* | training/src/anemoi/training/losses/kcrps.py |
| AnemoiAzureMLflowLogger* | training/src/anemoi/training/diagnostics/mlflow/azureml.py |
| AnemoiMLflowLogger* | training/src/anemoi/training/diagnostics/mlflow/logger.py |
| AnemoiProfiler* | training/src/anemoi/training/train/profiler.py |
| AnemoiTrainer* | training/src/anemoi/training/train/train.py |
| BaseAnemoiMLflowLogger* | training/src/anemoi/training/diagnostics/mlflow/logger.py |
| BaseGraphModule* | training/src/anemoi/training/train/tasks/base.py |
| BaseGridIndices* | training/src/anemoi/training/data/grid_indices.py |
| BaseLoss* | training/src/anemoi/training/losses/base.py |
| BaseMask | training/src/anemoi/training/utils/masks.py |
| BasePerBatchPlotCallback* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| BasePerEpochPlotCallback* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| BasePlotAdditionalMetrics* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| BasePlotCallback* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| BaseScaler* | training/src/anemoi/training/losses/scalers/base_scaler.py |
| BaseTendencyScaler* | training/src/anemoi/training/losses/scalers/variable_tendency.py |
| BaseUpdatingScaler* | training/src/anemoi/training/losses/scalers/base_scaler.py |
| BaseVariableLevelScaler* | training/src/anemoi/training/losses/scalers/variable_level.py |
| BaseVariableLossScaler* | training/src/anemoi/training/losses/scalers/variable.py |
| BenchmarkServer* | training/src/anemoi/training/diagnostics/benchmark_server.py |
| BenchmarkValue | training/src/anemoi/training/diagnostics/benchmark_server.py |
| Coastlines | training/src/anemoi/training/diagnostics/maps.py |
| CombinedLoss* | training/src/anemoi/training/losses/combined.py |
| CustomColormap* | training/src/anemoi/training/utils/custom_colormaps.py |
| DistinctipyColormap* | training/src/anemoi/training/utils/custom_colormaps.py |
| EnsemblePlotMixin | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| EquirectangularProjection | training/src/anemoi/training/diagnostics/maps.py |
| ExtractVariableGroupAndLevel | training/src/anemoi/training/utils/variables_metadata.py |
| FilteringLossWrapper* | training/src/anemoi/training/losses/filtering.py |
| FixedLengthSet | training/src/anemoi/training/diagnostics/mlflow/utils.py |
| FourierCorrelationLoss* | training/src/anemoi/training/losses/spatial.py |
| FrozenStateRecord | training/src/anemoi/training/losses/scaler_tensor.py |
| FullGrid* | training/src/anemoi/training/data/grid_indices.py |
| FunctionalLoss* | training/src/anemoi/training/losses/base.py |
| GeneralVariableLossScaler* | training/src/anemoi/training/losses/scalers/variable.py |
| GraphDiffusionForecaster* | training/src/anemoi/training/train/tasks/diffusionforecaster.py |
| GraphDiffusionTendForecaster* | training/src/anemoi/training/train/tasks/diffusionforecaster.py |
| GraphEnsForecaster* | training/src/anemoi/training/train/tasks/ensforecaster.py |
| GraphForecaster* | training/src/anemoi/training/train/tasks/forecaster.py |
| GraphInterpolator* | training/src/anemoi/training/train/tasks/interpolator.py |
| GraphNodeAttributeScaler* | training/src/anemoi/training/losses/scalers/node_attributes.py |
| GraphTrainableFeaturesPlot* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| GraphTrainableFeaturesPlot* | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| HuberLoss* | training/src/anemoi/training/losses/huber.py |
| KernelCRPS* | training/src/anemoi/training/losses/kcrps.py |
| LatLonData | training/src/anemoi/training/diagnostics/plots.py |
| LinearVariableLevelScaler* | training/src/anemoi/training/losses/scalers/variable_level.py |
| LocalBenchmarkServer* | training/src/anemoi/training/diagnostics/benchmark_server.py |
| LogCoshLoss* | training/src/anemoi/training/losses/logcosh.py |
| LogFFT2Distance* | training/src/anemoi/training/losses/spatial.py |
| LogsMonitor | training/src/anemoi/training/diagnostics/mlflow/logger.py |
| LongRolloutPlots* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| MAELoss* | training/src/anemoi/training/losses/mae.py |
| MaskedGrid* | training/src/anemoi/training/data/grid_indices.py |
| MatplotlibColormap* | training/src/anemoi/training/utils/custom_colormaps.py |
| MatplotlibColormapClevels* | training/src/anemoi/training/utils/custom_colormaps.py |
| MlFlowSync | training/src/anemoi/training/utils/mlflow_sync.py |
| MLFlowSystemSummarizer | training/src/anemoi/training/diagnostics/profilers.py |
| MSELoss* | training/src/anemoi/training/losses/mse.py |
| NaNMaskScaler* | training/src/anemoi/training/losses/scalers/loss_weights_mask.py |
| NoTendencyScaler* | training/src/anemoi/training/losses/scalers/variable_tendency.py |
| NoVariableLevelScaler* | training/src/anemoi/training/losses/scalers/variable_level.py |
| PlotHistogram* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| PlotHistogram* | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| PlotLoss* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| PlotLoss* | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| PlotSample* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| PlotSample* | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| PlotSpectrum* | training/src/anemoi/training/diagnostics/callbacks/plot.py |
| PlotSpectrum* | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| PolynomialVariableLevelScaler* | training/src/anemoi/training/losses/scalers/variable_level.py |
| Profile* | training/src/anemoi/training/commands/profiler.py |
| ReluVariableLevelScaler* | training/src/anemoi/training/losses/scalers/variable_level.py |
| RemoteBenchmarkServer* | training/src/anemoi/training/diagnostics/benchmark_server.py |
| ReweightedGraphNodeAttributeScaler* | training/src/anemoi/training/losses/scalers/node_attributes.py |
| RMSELoss* | training/src/anemoi/training/losses/rmse.py |
| Shape | training/src/anemoi/training/losses/scaler_tensor.py |
| StdevTendencyScaler* | training/src/anemoi/training/losses/scalers/variable_tendency.py |
| Train* | training/src/anemoi/training/commands/train.py |
| TrainBase* | training/src/anemoi/training/commands/train.py |
| VariableMaskingLossScaler* | training/src/anemoi/training/losses/scalers/variable_masking.py |
| VarTendencyScaler* | training/src/anemoi/training/losses/scalers/variable_tendency.py |
| WandBSystemSummarizer | training/src/anemoi/training/diagnostics/profilers.py |
| WeightedMSELoss* | training/src/anemoi/training/losses/weighted_mse.py |

> `*` indicates abstract base class (derives from ABC).  

Derived classes (explicit base list): 120
| Class | Base(s) | File |
| --- | --- | --- |
| AlmostFairKernelCRPSSchema | BaseLossSchema | training/src/anemoi/training/schemas/training.py |
| AnemoiCheckpoint | ModelCheckpoint | training/src/anemoi/training/diagnostics/callbacks/checkpoint.py |
| AnemoiDatasetsDataModule | pl.LightningDataModule | training/src/anemoi/training/data/datamodule/singledatamodule.py |
| AnemoiEnsDatasetsDataModule | AnemoiDatasetsDataModule | training/src/anemoi/training/data/datamodule/ensdatamodule.py |
| AvailableCallbacks | StrEnum | training/src/anemoi/training/losses/scalers/base_scaler.py |
| AzureIdentity | StrEnum | training/src/anemoi/training/diagnostics/mlflow/azureml.py |
| AzureMlflowSchema | MlflowSchema | training/src/anemoi/training/schemas/diagnostics.py |
| BaseDDPStrategySchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| BaseEnsemblePlotCallback | EnsemblePerBatchPlotMixin | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| BaseLossSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| BaseSchema | BaseModel | training/src/anemoi/training/schemas/base_schema.py |
| BaseTrainingSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| BenchmarkProfiler | Profiler | training/src/anemoi/training/diagnostics/profilers.py |
| BenchmarkProfilerSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| Boolean1DMask | torch.nn.Module, BaseMask | training/src/anemoi/training/utils/masks.py |
| Checkpoint | Command | training/src/anemoi/training/commands/checkpoint.py |
| Checkpoint | BaseModel | training/src/anemoi/training/schemas/hardware.py |
| CheckpointSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| CheckVariableOrder | pl.callbacks.Callback | training/src/anemoi/training/diagnostics/callbacks/sanity.py |
| CombinedLossSchema | BaseLossSchema | training/src/anemoi/training/schemas/training.py |
| ConfigGenerator | Command | training/src/anemoi/training/commands/config.py |
| CPUMonitor | BaseMetricsMonitor | training/src/anemoi/training/diagnostics/mlflow/system_metrics/cpu_monitor.py |
| CustomSystemMetricsMonitor | SystemMetricsMonitor | training/src/anemoi/training/diagnostics/mlflow/logger.py |
| DataLoaderSchema | PydanticBaseModel | training/src/anemoi/training/schemas/dataloader.py |
| DataModuleSchema | PydanticBaseModel | training/src/anemoi/training/schemas/datamodule.py |
| DataSchema | PydanticBaseModel | training/src/anemoi/training/schemas/data.py |
| DatasetSchema | PydanticBaseModel | training/src/anemoi/training/schemas/dataloader.py |
| DDPEnsGroupStrategy | DDPStrategy | training/src/anemoi/training/distributed/strategy.py |
| DDPEnsGroupStrategyStrategySchema | BaseDDPStrategySchema | training/src/anemoi/training/schemas/training.py |
| DDPGroupStrategy | DDPStrategy | training/src/anemoi/training/distributed/strategy.py |
| Debug | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| DiagnosticsSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| DiffusionForecasterSchema | ForecasterSchema | training/src/anemoi/training/schemas/training.py |
| DiffusionTendForecasterSchema | ForecasterSchema | training/src/anemoi/training/schemas/training.py |
| DistinctipyColormapSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| DummyProfiler | Profiler | training/src/anemoi/training/diagnostics/profilers.py |
| EarlyStopping | pl.callbacks.EarlyStopping | training/src/anemoi/training/diagnostics/callbacks/stopping.py |
| EarlyStoppingSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| EnsembleInitialConditions | nn.Module | training/src/anemoi/training/utils/inicond.py |
| EnsemblePerBatchPlotMixin | EnsemblePlotMixin | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| EnsNativeGridDataset | NativeGridDataset | training/src/anemoi/training/data/dataset/ensdataset.py |
| ExplicitTimes | BaseModel | training/src/anemoi/training/schemas/training.py |
| FilesSchema | PydanticBaseModel | training/src/anemoi/training/schemas/hardware.py |
| ForecasterEnsSchema | ForecasterSchema | training/src/anemoi/training/schemas/training.py |
| ForecasterSchema | BaseTrainingSchema | training/src/anemoi/training/schemas/training.py |
| Frequency | RootModel | training/src/anemoi/training/schemas/dataloader.py |
| FullGridIndicesSchema | BaseModel | training/src/anemoi/training/schemas/dataloader.py |
| GeneralVariableLossScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| GradientClip | BaseModel | training/src/anemoi/training/schemas/training.py |
| GraphNodeAttributeScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| GraphTrainableFeaturesPlotEnsSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| GraphTrainableFeaturesPlotSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| GreenGPUMonitor | BaseMetricsMonitor | training/src/anemoi/training/diagnostics/mlflow/system_metrics/gpu_monitor.py |
| HardwareSchema | BaseModel | training/src/anemoi/training/schemas/hardware.py |
| HuberLossSchema | BaseLossSchema | training/src/anemoi/training/schemas/training.py |
| ImplementedLossesUsingBaseLossSchema | str, Enum | training/src/anemoi/training/schemas/training.py |
| ImplementedStrategiesUsingBaseDDPStrategySchema | str, Enum | training/src/anemoi/training/schemas/training.py |
| InterpolationSchema | BaseTrainingSchema | training/src/anemoi/training/schemas/training.py |
| KernelCRPSSchema | BaseLossSchema | training/src/anemoi/training/schemas/training.py |
| LearningRateMonitor | pl_LearningRateMonitor | training/src/anemoi/training/diagnostics/callbacks/optimiser.py |
| LoaderSet | BaseModel | training/src/anemoi/training/schemas/dataloader.py |
| LogCosh | torch.autograd.Function | training/src/anemoi/training/losses/logcosh.py |
| LoggingSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| LoggingUnpickler | pickle.Unpickler | training/src/anemoi/training/utils/checkpoint.py |
| Logs | PydanticBaseModel | training/src/anemoi/training/schemas/hardware.py |
| LongRolloutPlotsSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| LossScalingSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| LR | BaseModel | training/src/anemoi/training/schemas/training.py |
| MaskedGridIndicesSchema | BaseModel | training/src/anemoi/training/schemas/dataloader.py |
| MatplotlibColormapClevelsSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| MatplotlibColormapSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| MemorySchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| MemorySnapshotRecorder | Callback | training/src/anemoi/training/diagnostics/callbacks/profiler.py |
| MlFlow | Command | training/src/anemoi/training/commands/mlflow.py |
| MlflowSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| NaNMaskScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| NativeGridDataset | IterableDataset | training/src/anemoi/training/data/dataset/singledataset.py |
| NoOutputMask | BaseMask | training/src/anemoi/training/utils/masks.py |
| OptimizerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| ParentUUIDCallback | Callback | training/src/anemoi/training/diagnostics/callbacks/provenance.py |
| PatchedProfile | profile | training/src/anemoi/training/diagnostics/profilers.py |
| PathsSchema | BaseModel | training/src/anemoi/training/schemas/hardware.py |
| PlotEnsHistogramSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotEnsLossSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotEnsSample | EnsemblePerBatchPlotMixin, _PlotSample | training/src/anemoi/training/diagnostics/callbacks/plot_ens.py |
| PlotEnsSampleSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotEnsSpectrumSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotHistogramSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotLossSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotSampleSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlotSpectrumSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| PlottingFrequency | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| ProfilerProgressBar | TQDMProgressBar | training/src/anemoi/training/diagnostics/profilers.py |
| Profiling | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| RedGPUMonitor | BaseMetricsMonitor | training/src/anemoi/training/diagnostics/mlflow/system_metrics/gpu_monitor.py |
| RegisterMigrations | Callback | training/src/anemoi/training/utils/checkpoint.py |
| ReweightedGraphNodeAttributeScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| Rollout | BaseModel | training/src/anemoi/training/schemas/training.py |
| RolloutEval | Callback | training/src/anemoi/training/diagnostics/callbacks/evaluation.py |
| RolloutEvalEns | RolloutEval | training/src/anemoi/training/diagnostics/callbacks/evaluation.py |
| ScaleTensor | nn.Module | training/src/anemoi/training/losses/scaler_tensor.py |
| Snapshot | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| StochasticWeightAveraging | pl_StochasticWeightAveraging | training/src/anemoi/training/diagnostics/callbacks/optimiser.py |
| StrEncoder | JSONEncoder | training/src/anemoi/training/diagnostics/mlflow/azureml.py |
| StrEncoder | JSONEncoder | training/src/anemoi/training/diagnostics/mlflow/logger.py |
| StrEnum | str, Enum | training/src/anemoi/training/losses/scalers/base_scaler.py |
| SWA | BaseModel | training/src/anemoi/training/schemas/training.py |
| TargetForcing | BaseModel | training/src/anemoi/training/schemas/training.py |
| TendencyScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| TendencyScalerTargets | str, Enum | training/src/anemoi/training/schemas/training.py |
| TensorboardSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| TensorDim | IntEnum | training/src/anemoi/training/utils/enums.py |
| TimeLimit | pl.callbacks.Callback | training/src/anemoi/training/diagnostics/callbacks/stopping.py |
| TimeLimitSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
| UnvalidatedBaseSchema | PydanticBaseModel | training/src/anemoi/training/schemas/base_schema.py |
| VariableLevelScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| VariableLevelScalerTargets | str, Enum | training/src/anemoi/training/schemas/training.py |
| VariableMaskingScalerSchema | BaseModel | training/src/anemoi/training/schemas/training.py |
| WandbSchema | BaseModel | training/src/anemoi/training/schemas/diagnostics.py |
