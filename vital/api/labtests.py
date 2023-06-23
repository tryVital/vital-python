from typing import Dict, Mapping, Optional

from vital.api.api import API


class LabTests(API):
    """V3 endpoints for managing testkit orders."""

    def create_order(
        self,
        user_id: str,
        patient_details: Dict,
        patient_address: Dict,
        lab_test_id: str,
        physician: Optional[Dict],
        health_insurance: Optional[Dict] = None,
        priority: Optional[bool] = None,
    ) -> Mapping[str, str]:
        """Create new order"""
        params = {
            "user_id": user_id,
            "patient_details": patient_details,
            "patient_address": patient_address,
            "lab_test_id": lab_test_id,
            "physician": physician,
        }
        if health_insurance:
            params["health_insurance"] = health_insurance
        if priority:
            params["priority"] = priority

        return self.client.post("/order", params, api_version="v3")
    
    def create_test(
        self,
        name: str,
        description: str,
        markers: list[str],
        lab_id: int,
        method: str,
        sample_type: str,
    ) -> Mapping[str, str]:
        """Create new lab test"""
        params = {
            "name": name,
            "description": description,
            "lab_id": lab_id,
            "method": method,
            "sample_type": sample_type,
            "marker_ids": markers,
        }

        return self.client.post("/lab_tests", params, api_version="v3")

    def get_orders(self, page: int = 1, size: int = 50) -> Mapping[str, str]:
        """Get all orders"""
        return self.client.get(
            "/orders",
            {"page": page, "size": size},
            api_version="v3",
        )

    def get_order(self, order_id: str) -> Mapping[str, str]:
        """
        Get order status.
        :param str user_id: The order_id.
        """
        return self.client.get(f"/order/{order_id}", api_version="v3")

    def cancel_order(self, order_id: str) -> Mapping[str, str]:
        """
        Cancel order.
        :param str user_id: The order_id.
        """
        return self.client.post(f"/order/{order_id}/cancel", api_version="v3")

    def get_tests(self) -> Mapping[str, str]:
        """
        GET all lab tests the team has access to.
        """
        return self.client.get("/lab_tests")

    def get_results(self, order_id: str) -> Mapping[str, str]:
        """
        GET both metadata and raw json test data.
        """
        return self.client.get(f"/order/{order_id}/result", api_version="v3")

    def get_results_pdf(self, order_id: str) -> Mapping[str, str]:
        """
        GET gets the lab result for the order in PDF format.
        """
        return self.client.get(f"/order/{order_id}/result/pdf", api_version="v3")

    def get_results_metadata(self, order_id: str) -> Mapping[str, str]:
        """
        GET metadata related to order results, such as
        lab metadata, provider and sample dates.
        """
        return self.client.get(f"/order/{order_id}/result/metadata", api_version="v3")

    def get_area_info(self, zip_code: str) -> Mapping[str, str]:
        """
        GET area info for a given zip code.
        """
        return self.client.get("/area/info", {"zip_code": zip_code}, api_version="v3")
