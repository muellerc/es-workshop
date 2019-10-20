+++
title = "Provisioning Amazon Elasticsearch Service"
draft = true
weight = 30
pre = "3. "
+++

If you use Windows, be sure Python is on your PATH. To see if it is, type `python`
at a command prompt. The easiest way to make sure Python is on your PATH is to tick the
**Add Python 3.x to PATH** checkbox on the first screen of the Python installer wizard.
If you already have Python installed, but it's not on your PATH, you can add it by
editing the `PATH` environment variable. 


{{% notice tip %}}
Install **jq** to convert the received JSON into a nicely formatted one.
```bash
brew install jq
,,,
After you have installed jq, append ** | jq '.'** to your curl command.
{{% /notice %}}


curl -k -XGET "https://localhost:9200/_cat/health?v"

curl -k -XGET "https://localhost:9200/_cat/nodes?v"

curl -k -XGET "https://localhost:9200/_cat/indices?v"


GET /_cluster/health?pretty

{
  "cluster_name": "689573718314:elastic-search-domain-olp",
  "status": "green",
  "timed_out": false,
  "number_of_nodes": 5,
  "number_of_data_nodes": 2,
  "discovered_master": true,
  "active_primary_shards": 1,
  "active_shards": 2,
  "relocating_shards": 0,
  "initializing_shards": 0,
  "unassigned_shards": 0,
  "delayed_unassigned_shards": 0,
  "number_of_pending_tasks": 0,
  "number_of_in_flight_fetch": 0,
  "task_max_waiting_in_queue_millis": 0,
  "active_shards_percent_as_number": 100
}


GET /_cluster/state

{
  "cluster_name": "689573718314:elastic-search-domain-olp",
  "cluster_uuid": "KIgoKFIcT0-xAih3ZGCwEA",
  "version": 49,
  "state_uuid": "LimwdT9CRl22QRPc5hQfEw",
  "master_node": "j7LGU91jTkecNxSeaKbNHQ",
  "blocks": {},
  "nodes": {
    "evWCi38dRL2VyGZsM8A1BA": {
      "name": "0201a7442e66d37f8fa671f684fda372",
      "ephemeral_id": "AwdBvEutTj6qk8DPyODM1g"
    },
    "SUoBpB2hQPKiNTr-xRO8LA": {
      "name": "2f712f19ee7e4c7af0accde9293dc9bb",
      "ephemeral_id": "6_hzdvEsRC-EXYkCkBAj6Q"
    },
    "74z-XcFrR6ymyRFgyYPpXg": {
      "name": "e747296f43e09cb9e3eb55250647588e",
      "ephemeral_id": "2G8werdcQveYaGncLMDhTA"
    },
    "MgU8NwgoQcOXrnZpsw4tWw": {
      "name": "aa7a38ac10b6784cd0e0cdeae3d30791",
      "ephemeral_id": "irjm9yOTTI2_YkTG47dD6A"
    },
    "j7LGU91jTkecNxSeaKbNHQ": {
      "name": "60bac0968ce3f40a630b8ddbb3d08018",
      "ephemeral_id": "gZRYtiQvSjuqCkiKTGGv8A"
    }
  },
  "metadata": {
    "cluster_uuid": "KIgoKFIcT0-xAih3ZGCwEA",
    "cluster_coordination": {
      "term": 4,
      "last_committed_config": [
        "MgU8NwgoQcOXrnZpsw4tWw",
        "SUoBpB2hQPKiNTr-xRO8LA",
        "j7LGU91jTkecNxSeaKbNHQ"
      ],
      "last_accepted_config": [
        "MgU8NwgoQcOXrnZpsw4tWw",
        "SUoBpB2hQPKiNTr-xRO8LA",
        "j7LGU91jTkecNxSeaKbNHQ"
      ],
      "voting_config_exclusions": []
    },
    "templates": {},
    "indices": {
      ".kibana_1": {
        "state": "open",
        "settings": {
          "index": {
            "number_of_shards": "1",
            "auto_expand_replicas": "0-1",
            "provided_name": ".kibana_1",
            "creation_date": "1571386406563",
            "number_of_replicas": "1",
            "uuid": "ULxEMv8XS1aiOmRhhsuC7g",
            "version": {
              "created": "7010199"
            }
          }
        },
        "mappings": {
          "_doc": {
            "_meta": {
              "migrationMappingPropertyHashes": {
                "server": "ec97f1c5da1a19609a60874e5af1100c",
                "visualization": "52d7a13ad68a150c4525b292d23e12cc",
                "references": "7997cf5a56cc02bdc9c93361bde732b0",
                "kql-telemetry": "d12a98a6f19a2d273696597547e064ee",
                "type": "2f4316de49999235636386fe51dc06c1",
                "url": "c7f66a0df8b1b52f17c28c4adb111105",
                "migrationVersion": "4a1746014a75ade3a714e1db5763276f",
                "index-pattern": "66eccb05066c5a89924f48a9e9736499",
                "search": "181661168bbadd1eff5902361e2a0d5c",
                "updated_at": "00da57df13e94e9d98437d13ace4bfe0",
                "namespace": "2f4316de49999235636386fe51dc06c1",
                "timelion-sheet": "9a2a2748877c7a7b582fef201ab1d4cf",
                "config": "87aca8fdb053154f11383fce3dbf3edf",
                "dashboard": "eb3789e1af878e73f85304333240f65f"
              }
            },
            "dynamic": "strict",
            "properties": {
              "server": {
                "properties": {
                  "uuid": {
                    "type": "keyword"
                  }
                }
              },
              "visualization": {
                "properties": {
                  "savedSearchRefName": {
                    "type": "keyword"
                  },
                  "description": {
                    "type": "text"
                  },
                  "uiStateJSON": {
                    "type": "text"
                  },
                  "title": {
                    "type": "text"
                  },
                  "version": {
                    "type": "integer"
                  },
                  "kibanaSavedObjectMeta": {
                    "properties": {
                      "searchSourceJSON": {
                        "type": "text"
                      }
                    }
                  },
                  "visState": {
                    "type": "text"
                  }
                }
              },
              "references": {
                "type": "nested",
                "properties": {
                  "name": {
                    "type": "keyword"
                  },
                  "id": {
                    "type": "keyword"
                  },
                  "type": {
                    "type": "keyword"
                  }
                }
              },
              "kql-telemetry": {
                "properties": {
                  "optInCount": {
                    "type": "long"
                  },
                  "optOutCount": {
                    "type": "long"
                  }
                }
              },
              "type": {
                "type": "keyword"
              },
              "url": {
                "properties": {
                  "accessCount": {
                    "type": "long"
                  },
                  "accessDate": {
                    "type": "date"
                  },
                  "url": {
                    "type": "text",
                    "fields": {
                      "keyword": {
                        "ignore_above": 2048,
                        "type": "keyword"
                      }
                    }
                  },
                  "createDate": {
                    "type": "date"
                  }
                }
              },
              "migrationVersion": {
                "dynamic": "true",
                "type": "object"
              },
              "index-pattern": {
                "properties": {
                  "notExpandable": {
                    "type": "boolean"
                  },
                  "fieldFormatMap": {
                    "type": "text"
                  },
                  "sourceFilters": {
                    "type": "text"
                  },
                  "typeMeta": {
                    "type": "keyword"
                  },
                  "timeFieldName": {
                    "type": "keyword"
                  },
                  "intervalName": {
                    "type": "keyword"
                  },
                  "fields": {
                    "type": "text"
                  },
                  "title": {
                    "type": "text"
                  },
                  "type": {
                    "type": "keyword"
                  }
                }
              },
              "search": {
                "properties": {
                  "hits": {
                    "type": "integer"
                  },
                  "columns": {
                    "type": "keyword"
                  },
                  "description": {
                    "type": "text"
                  },
                  "sort": {
                    "type": "keyword"
                  },
                  "title": {
                    "type": "text"
                  },
                  "version": {
                    "type": "integer"
                  },
                  "kibanaSavedObjectMeta": {
                    "properties": {
                      "searchSourceJSON": {
                        "type": "text"
                      }
                    }
                  }
                }
              },
              "updated_at": {
                "type": "date"
              },
              "namespace": {
                "type": "keyword"
              },
              "timelion-sheet": {
                "properties": {
                  "hits": {
                    "type": "integer"
                  },
                  "timelion_sheet": {
                    "type": "text"
                  },
                  "timelion_interval": {
                    "type": "keyword"
                  },
                  "timelion_columns": {
                    "type": "integer"
                  },
                  "timelion_other_interval": {
                    "type": "keyword"
                  },
                  "timelion_rows": {
                    "type": "integer"
                  },
                  "description": {
                    "type": "text"
                  },
                  "title": {
                    "type": "text"
                  },
                  "version": {
                    "type": "integer"
                  },
                  "kibanaSavedObjectMeta": {
                    "properties": {
                      "searchSourceJSON": {
                        "type": "text"
                      }
                    }
                  },
                  "timelion_chart_height": {
                    "type": "integer"
                  }
                }
              },
              "config": {
                "dynamic": "true",
                "properties": {
                  "buildNum": {
                    "type": "keyword"
                  }
                }
              },
              "dashboard": {
                "properties": {
                  "hits": {
                    "type": "integer"
                  },
                  "timeFrom": {
                    "type": "keyword"
                  },
                  "timeTo": {
                    "type": "keyword"
                  },
                  "refreshInterval": {
                    "properties": {
                      "display": {
                        "type": "keyword"
                      },
                      "section": {
                        "type": "integer"
                      },
                      "value": {
                        "type": "integer"
                      },
                      "pause": {
                        "type": "boolean"
                      }
                    }
                  },
                  "description": {
                    "type": "text"
                  },
                  "uiStateJSON": {
                    "type": "text"
                  },
                  "timeRestore": {
                    "type": "boolean"
                  },
                  "title": {
                    "type": "text"
                  },
                  "version": {
                    "type": "integer"
                  },
                  "kibanaSavedObjectMeta": {
                    "properties": {
                      "searchSourceJSON": {
                        "type": "text"
                      }
                    }
                  },
                  "optionsJSON": {
                    "type": "text"
                  },
                  "panelsJSON": {
                    "type": "text"
                  }
                }
              }
            }
          }
        },
        "aliases": [
          ".kibana"
        ],
        "primary_terms": {
          "0": 2
        },
        "in_sync_allocations": {
          "0": [
            "-mLbyigsRve2QGs9In45dQ",
            "RXvO-GrDROGA4SJftANmyA"
          ]
        }
      }
    },
    "index-graveyard": {
      "tombstones": []
    },
    "repositories": {
      "cs-automated-enc": {
        "type": "s3"
      }
    }
  },
  "routing_table": {
    "indices": {
      ".kibana_1": {
        "shards": {
          "0": [
            {
              "state": "STARTED",
              "primary": true,
              "node": "74z-XcFrR6ymyRFgyYPpXg",
              "relocating_node": null,
              "shard": 0,
              "index": ".kibana_1",
              "allocation_id": {
                "id": "-mLbyigsRve2QGs9In45dQ"
              }
            },
            {
              "state": "STARTED",
              "primary": false,
              "node": "evWCi38dRL2VyGZsM8A1BA",
              "relocating_node": null,
              "shard": 0,
              "index": ".kibana_1",
              "allocation_id": {
                "id": "RXvO-GrDROGA4SJftANmyA"
              }
            }
          ]
        }
      }
    }
  },
  "routing_nodes": {
    "unassigned": [],
    "nodes": {
      "74z-XcFrR6ymyRFgyYPpXg": [
        {
          "state": "STARTED",
          "primary": true,
          "node": "74z-XcFrR6ymyRFgyYPpXg",
          "relocating_node": null,
          "shard": 0,
          "index": ".kibana_1",
          "allocation_id": {
            "id": "-mLbyigsRve2QGs9In45dQ"
          }
        }
      ],
      "evWCi38dRL2VyGZsM8A1BA": [
        {
          "state": "STARTED",
          "primary": false,
          "node": "evWCi38dRL2VyGZsM8A1BA",
          "relocating_node": null,
          "shard": 0,
          "index": ".kibana_1",
          "allocation_id": {
            "id": "RXvO-GrDROGA4SJftANmyA"
          }
        }
      ]
    }
  },
  "snapshots": {
    "snapshots": []
  }
}


GET /_cluster/stats?human&pretty

{
  "_nodes": {
    "total": 5,
    "successful": 5,
    "failed": 0
  },
  "cluster_name": "689573718314:elastic-search-domain-olp",
  "cluster_uuid": "KIgoKFIcT0-xAih3ZGCwEA",
  "timestamp": 1571396536772,
  "status": "green",
  "indices": {
    "count": 1,
    "shards": {
      "total": 2,
      "primaries": 1,
      "replication": 1,
      "index": {
        "shards": {
          "min": 2,
          "max": 2,
          "avg": 2
        },
        "primaries": {
          "min": 1,
          "max": 1,
          "avg": 1
        },
        "replication": {
          "min": 1,
          "max": 1,
          "avg": 1
        }
      }
    },
    "docs": {
      "count": 1,
      "deleted": 0
    },
    "store": {
      "size": "7.6kb",
      "size_in_bytes": 7794
    },
    "fielddata": {
      "memory_size": "0b",
      "memory_size_in_bytes": 0,
      "evictions": 0
    },
    "query_cache": {
      "memory_size": "0b",
      "memory_size_in_bytes": 0,
      "total_count": 0,
      "hit_count": 0,
      "miss_count": 0,
      "cache_size": 0,
      "cache_count": 0,
      "evictions": 0
    },
    "completion": {
      "size": "0b",
      "size_in_bytes": 0
    },
    "segments": {
      "count": 2,
      "memory": "2.3kb",
      "memory_in_bytes": 2386,
      "terms_memory": "1.5kb",
      "terms_memory_in_bytes": 1622,
      "stored_fields_memory": "624b",
      "stored_fields_memory_in_bytes": 624,
      "term_vectors_memory": "0b",
      "term_vectors_memory_in_bytes": 0,
      "norms_memory": "0b",
      "norms_memory_in_bytes": 0,
      "points_memory": "4b",
      "points_memory_in_bytes": 4,
      "doc_values_memory": "136b",
      "doc_values_memory_in_bytes": 136,
      "index_writer_memory": "0b",
      "index_writer_memory_in_bytes": 0,
      "version_map_memory": "0b",
      "version_map_memory_in_bytes": 0,
      "fixed_bit_set": "96b",
      "fixed_bit_set_memory_in_bytes": 96,
      "max_unsafe_auto_id_timestamp": -1,
      "file_sizes": {}
    }
  },
  "nodes": {
    "count": {
      "total": 5,
      "data": 2,
      "coordinating_only": 0,
      "master": 3,
      "ingest": 2
    },
    "versions": [
      "7.1.1"
    ],
    "os": {
      "available_processors": 10,
      "allocated_processors": 10,
      "names": [
        {
          "count": 5
        }
      ],
      "pretty_names": [
        {
          "count": 5
        }
      ],
      "mem": {
        "total": "37.5gb",
        "total_in_bytes": 40298311680,
        "free": "1.2gb",
        "free_in_bytes": 1367736320,
        "used": "36.2gb",
        "used_in_bytes": 38930575360,
        "free_percent": 3,
        "used_percent": 97
      }
    },
    "process": {
      "cpu": {
        "percent": 0
      },
      "open_file_descriptors": {
        "min": 840,
        "max": 862,
        "avg": 849
      }
    },
    "jvm": {
      "max_uptime": "2.3h",
      "max_uptime_in_millis": 8516171,
      "mem": {
        "heap_used": "1.3gb",
        "heap_used_in_bytes": 1433052416,
        "heap_max": "22.9gb",
        "heap_max_in_bytes": 24608899072
      },
      "threads": 374
    },
    "fs": {
      "total": "40.3gb",
      "total_in_bytes": 43318788096,
      "free": "33.7gb",
      "free_in_bytes": 36227321856,
      "available": "33.6gb",
      "available_in_bytes": 36143435776
    },
    "network_types": {
      "transport_types": {
        "com.amazon.opendistroforelasticsearch.security.ssl.http.netty.OpenDistroSecuritySSLNettyTransport": 5
      },
      "http_types": {
        "filter-jetty": 5
      }
    },
    "discovery_types": {
      "zen": 5
    }
  }
}

GET /_cluster/pending_tasks

{
  "tasks": []
}

GET /_nodes

...

GET /_nodes/stats

...

GET /_nodes/nodeId1,nodeId2/stats

...




GET /_search



https://elasticsearch-cheatsheet.jolicode.com/
https://lzone.de/cheat-sheet/ElasticSearch