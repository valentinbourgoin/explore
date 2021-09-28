from celery.result import AsyncResult
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication, permissions

class TasksView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, task_id):
        task_result = AsyncResult(task_id)
        result = {
            "task_id": task_id,
            "task_status": task_result.status,
            "task_result": task_result.result
        }
        if (task_result.result and task_result.result['subtasks']):
            result['subtask_results'] = []
            for subtask in task_result.result['subtasks']:
                s = AsyncResult(subtask)
                # @todo DRY PLZ
                result['subtask_results'].append({
                    "task_id": subtask,
                    "task_status": s.status,
                    "task_result": s.result
                })
        return Response(result)