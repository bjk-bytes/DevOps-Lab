#!/bin/bash
echo "Hello, World from Jenkins!"
echo "Build number: $BUILD_NUMBER"
echo "Job name: $JOB_NAME"
echo "Workspace: $WORKSPACE"
echo "Built at: $(date -u +'%Y-%m-%dT%H:%M:%SZ')"
