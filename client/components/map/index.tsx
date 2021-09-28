import React from 'react'

import { MapContainer, TileLayer, Polyline, GeoJSON } from 'react-leaflet'

import 'leaflet/dist/leaflet.css'
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css'
import "leaflet-defaulticon-compatibility";

const Map:React.FC = (props) => {
    const { grid, tiles: { features = [] } } = props

    const getCenterCoordinates = (grid) => {
        if (grid.center_point) {
            // We need to reverse coordinates because GeoJSON use (long, lat)
            return grid.center_point.coordinates.reverse()
        }
        return [0., 0.]
    }

    const mapStyle = (feature) => {
        const isTileLocked = (feature) => {
            return feature.properties.status === 1
        }

        const isTileLockedByUser = (feature) => {
            // @todo
            return isTileLocked(feature) 
                && feature.properties.activity_related.user.username === 'valentin'
        }

        const getTileColor = (feature) => {
            if (isTileLockedByUser(feature)) {
                return '#E6B91E' // @todo Use theme
            } else if (isTileLocked(feature)) {
                return '#fc4103'
            }
            return '#666'
        }

        return ({
            color: getTileColor(feature),
            weight: 1,
            opacity: (isTileLocked(feature)) ? .7 : .9
          });
    }

    return (
        <>
        { grid &&
            <MapContainer center={getCenterCoordinates(grid)} zoom={13} scrollWheelZoom={false}>
                <GeoJSON 
                    data={features} 
                    style={mapStyle}
                />
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                    attribution="&copy; <a href=&quot;http://osm.org/copyright&quot;>OpenStreetMap</a> contributors"
                />
            </MapContainer>
        }
        </>
    )
}

export default Map